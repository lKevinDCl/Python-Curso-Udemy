texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

print(texto.lstrip(",:_#"))

#lstrip es un metodo que permite eliminar espacios de izquierda a derecha

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, "naranja")

print(frutas)

#El metodo insert permite editar una lista mediante aprametros.

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)