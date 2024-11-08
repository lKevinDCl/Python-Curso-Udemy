

mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print ('No sé qué animal tienes')


edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if edad >= 18 and tiene_licencia == True:
    print(f"Puedes conducir")
elif edad >= 18 and tiene_licencia == False:
    print(f"No puedes conducir. Necesitas contar con una licencia")
else:
    print(f"No puedes conducir aún. Debes tener 18 años y contar con una licencia")

habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

if (habla_ingles == True and sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif (habla_ingles == False and sabe_python == False):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif (habla_ingles == False and sabe_python == True):
    print("Para postularte, necesitas tener conocimientos de inglés")
elif (habla_ingles == True and sabe_python == False):
    print("Para postularte, necesitas saber programar en Python")


