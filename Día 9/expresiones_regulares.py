import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

"""palabra = 'ayuda' in texto

print(palabra)"""

"""patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda)

"""

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron, texto)

print(resultado.group())
print(resultado.group(2))

"""
Práctica Módulo RE 1
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
"""

import re

import re


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

"""
Práctica Módulo RE 2
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
"""
import re


def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")

"""

Práctica Módulo RE 3
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
"""
import re


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")