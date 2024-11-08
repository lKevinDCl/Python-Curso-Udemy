#text = "Hola mundO me encantA pYthon"
#letters = "a,b,c"

text = input("Inserta un texto que quieras \n")
letters = input("Inserta tres letras separadas por comas: \n")

lista_texto_lower = text.lower()
lista_letters = letters.split(',')

print(f"tu palabra es: \n{lista_texto_lower}")

#Cuantas veces aparece una de las letras en el texto (puede que necesitemos poner todas en minusculas)

print(f"La letra {lista_letters[0]} se repite {lista_texto_lower.count(lista_letters[0])}")
print(f"La letra {lista_letters[1]} se repite {lista_texto_lower.count(lista_letters[1])}")
print(f"La letra {lista_letters[2]} se repite {lista_texto_lower.count(lista_letters[2])}")


#Cuantas palabras hay en total en todo el texto
lista_texto = lista_texto_lower.split()
print(f"El numero de palabras en tu texto es de: \n{len(lista_texto)}")

#Nos debe traer la primera y la ultima letra
print(f"la primera letra de tu texto es: '{lista_texto_lower[0]}' y la ultima letras es: '{lista_texto_lower[-1]}'")

#Nos debe invertir las palabras, mas no el orden y deben ser unidas por espacios
lista_texto.reverse()
print(f"El texto invertido es: \n{" ".join(lista_texto)}")

#Verificar si la palabra python existe en el texto

print(f"La letra python se encuentra en el texto: \n{'python' in lista_texto}")


