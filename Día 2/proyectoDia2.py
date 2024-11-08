nombre = input("Hola!, Con quien tengo el gusto? \n*inserte su nombre* \n")
ventas = input("cuanto has vendido en el mes?: \n")
comision = round(float(ventas)*.13,2)

print(f"Okay {nombre} este mes, ganaste ${comision} pejitos")