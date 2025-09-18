#import datetime


#Me permite poder manejar las horas en el formato que necesite
#Usa el formato de 24 Hrs
'''mi_hora = datetime.time(17,35,50,1500)
print(mi_hora)'''


#Me permite manejar dia en formato YYYY-MM-DD
#Cuenta con metodos para saber el dia actual en base al sistema
'''
mi_dia = datetime.date(2025,10,17)

print(mi_dia)
print(mi_dia.today())
'''



'''from datetime import datetime # Aunque parezca similar es diferente

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
mi_fecha = mi_fecha.replace(month= 6)

print(mi_fecha)
'''


#Este es un ejemplo de cuanto tiempo vivio una persona
'''
from datetime import date

nacimiento = date (2004,5,26)
defuncion = date (2080,8,18)

vida = defuncion - nacimiento
print(vida)'''


# Este es un ejemplo de codigo qque nos permite saber cuanto durmio una persona

#from datetime import datetime

#depierta = datetime (2022,10,5,7,30)
#duerme = datetime (2022,10,5,23,45)

#vigilia = duerme - depierta

#print (vigilia.seconds)

'''
Práctica Módulo Datetime 1
Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
'''

#from datetime import date

#mi_fecha = date(1999,2,3)

'''
Práctica Módulo Datetime 2
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
'''

#from datetime import date

#hoy = date.today()

#print(hoy)

'''

Práctica Módulo Datetime 3
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
'''

from datetime import datetime
hoy = datetime.today()
minutos = hoy.minute

print(minutos)
