monedas = 5

while monedas > 0:
    print (f"Tengo {monedas} monedas")
    monedas -= 1

else : print("no tengo mas dinero :(")

numero = 50

while numero > -1:
    if numero % 5 == 0:
        print(f"El numero es: {numero}")
    numero -= 1

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for i in lista_numeros:
    if i < 0:
        continue
    print(i)