#ejemplo del video
def multiplicar (numero1, numero2):
    #return numero1 * numero2

    total = numero1 * numero2
    return total

#print(multiplicar(5,10))

resultado = multiplicar(5,10)
print(resultado)

#Practicas:

'''
    Práctica Return 1
Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:

'''

def potencia(num1, num2):
    return num1**num2

resultado = potencia(2,3)

print(resultado)

'''

Práctica Return 2
Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.

'''

def usd_a_eur(usd):
    return usd*0.90

dolares = 10

resultado = usd_a_eur(dolares)
print(resultado)

'''

Práctica Return 3
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

'''

def invertir_palabra(palabra):
    return "".join(reversed(palabra.upper()))

palabra = "Kevin"

resultado = invertir_palabra(palabra)

print(resultado)