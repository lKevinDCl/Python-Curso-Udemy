from django.urls import path
from .views import (
    PrediccionDemandaAPIView,
    PedidoListCreateAPIView,
    PedidoRetrieveUpdateDestroyAPIView,
    ModeloListAPIView,
    HistoricoDemandaAPIView,
    ModeloRetrieveAPIView,
    GenerarCotizacionAPIView
)

urlpatterns = [
    path('prediccion/', PrediccionDemandaAPIView.as_view(), name='prediccion-api'),

    path('pedidos/', PedidoListCreateAPIView.as_view(), name='pedido-list-create'),
    path('pedidos/<int:id_pedido>/', PedidoRetrieveUpdateDestroyAPIView.as_view(), name='pedido-detail'),

    path('modelos/', ModeloListAPIView.as_view(), name='modelos-list'),
    path('historico-demanda/', HistoricoDemandaAPIView.as_view(), name='historico-demanda'),

    path('modelos/<int:id_modelo>/', ModeloRetrieveAPIView.as_view(), name='modelo-detail'),

    path('cotizacion/', GenerarCotizacionAPIView.as_view(), name='generar-cotizacion'),
]
