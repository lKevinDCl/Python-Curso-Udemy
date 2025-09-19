from datetime import datetime
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from .models import Modelo, Pedido
from .serializers import ( PedidoSerializer, ModeloSerializer, )
from .modelo_prediccion import predecir_demanda
from django.db.models.functions import TruncMonth
from dateutil.relativedelta import relativedelta

from .models import Modelo, Tela, Cierre, Hilo, Boton, Costura

class ModeloRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    lookup_field = 'id_modelo'

class ModeloListAPIView(generics.ListAPIView):

    queryset = Modelo.objects.filter(activo=True)
    serializer_class = ModeloSerializer

class HistoricoDemandaAPIView(APIView):
    def get(self, request):
        meses = request.query_params.get('meses', 12)
        modelo_id_raw = request.query_params.get('modelo_id', None)

        try:
            meses = int(meses)
        except ValueError:
            return Response({"error": "Parámetro 'meses' inválido"}, status=400)

        pedidos = Pedido.objects.all()

        if modelo_id_raw:
            try:
                modelo_id = int(modelo_id_raw)
                pedidos = pedidos.filter(id_modelo=modelo_id)
            except ValueError:
                return Response({"error": "modelo_id debe ser un entero"}, status=400)

        pedidos = pedidos.annotate(
            fecha=TruncMonth('fecha_pedido')
        ).values('fecha').annotate(
            total=Sum('cantidad')
        ).filter(
            fecha__isnull=False
        ).order_by('-fecha')

        pedidos = list(pedidos)[:meses]

        labels = [pedido['fecha'].strftime("%Y-%m") for pedido in reversed(pedidos)]
        data = [pedido['total'] for pedido in reversed(pedidos)]

        return Response({
            "success": True,
            "data": {
                "labels": labels,
                "data": data
            }
        })
        
class PrediccionDemandaAPIView(APIView):
    def post(self, request):
        try:
            id_modelo = request.data.get('id_modelo')

            if not id_modelo:
                return Response({'error': 'id_modelo es requerido'}, status=status.HTTP_400_BAD_REQUEST)

            now = datetime.now()
            predicciones = []
            etiquetas = []

            for i in range(1, 4):  # Próximos 3 meses
                fecha_futura = now + relativedelta(months=i)
                year = fecha_futura.year
                month = fecha_futura.month

                pred = predecir_demanda(id_modelo, year, month)
                predicciones.append(pred)
                etiquetas.append(fecha_futura.strftime('%Y-%m'))

            return Response({
                'labels': etiquetas,
                'data': predicciones
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GenerarCotizacionAPIView(APIView):
    def post(self, request):
        id_modelo = request.data.get("id_modelo")
        cantidad = int(request.data.get("cantidad", 1))

        try:
            modelo = Modelo.objects.get(id_modelo=id_modelo)
        except Modelo.DoesNotExist:
            return Response({"error": "Modelo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            tela = Tela.objects.first()
            cierre = Cierre.objects.first()
            hilo = Hilo.objects.first()
            boton = Boton.objects.first()
            costura = Costura.objects.first()
        except Exception:
            return Response({"error": "No hay materiales registrados."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        metros_tela = 1.5
        metros_hilo = 2
        cantidad_botones = 4
        cantidad_costuras = 1
        cantidad_cierres = 1

        costo_tela = float(tela.precio_por_metro) * metros_tela
        costo_hilo = float(hilo.precio) * metros_hilo
        costo_boton = float(boton.precio) * cantidad_botones
        costo_costura = float(costura.precio) * cantidad_costuras
        costo_cierre = float(cierre.precio) * cantidad_cierres
        
        mano_obra = float(modelo.precio_base) * 0.3

        desglose = {
            "tela": round(costo_tela, 2),
            "cierre": round(costo_cierre, 2),
            "hilo": round(costo_hilo, 2),
            "botones": round(costo_boton, 2),
            "costura": round(costo_costura, 2),
            "mano_obra": round(mano_obra, 2)
        }

        total_unitario = sum(desglose.values())
        total_general = total_unitario * cantidad
        
        precio_sugerido = total_unitario * 1.1

        porcentajes = {
            k: f"{(v / total_unitario) * 100:.0f}%" for k, v in desglose.items()
        }

        return Response({
            "desglose": desglose,
            "porcentajes": porcentajes,
            "costo_unitario": round(total_unitario, 2),
            "costo_total": round(total_general, 2),
            "precio_sugerido": round(precio_sugerido, 2)
        })

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20  
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response({
            'success': True,
            'data': data,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link()
        })

class PedidoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PedidoSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        return Pedido.objects.select_related('id_cliente', 'id_modelo')\
                           .only('id_pedido', 'cantidad', 'fecha_pedido', 'total', 'estado', 
                                 'id_cliente__nombre', 'id_modelo__nombre_modelo', 'created_at')\
                           .order_by('-fecha_pedido')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

class PedidoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PedidoSerializer
    lookup_field = 'id_pedido'
    
    def get_queryset(self):
        return Pedido.objects.select_related('id_cliente', 'id_modelo')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'success': True,
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'message': 'Pedido eliminado correctamente'
        }, status=status.HTTP_204_NO_CONTENT)
    


