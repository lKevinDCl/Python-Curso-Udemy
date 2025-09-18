from fileinput import close

import bs4
import requests
from urllib3 import request

#resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
resultado =requests.get('https://www.escueladirecta.com/l/products')

# print(resultado.text)
"""
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())"""

"""parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)"""

"""columna_lateral = sopa.select('.content p')
print(columna_lateral)

for p in columna_lateral:
    print(p.getText())"""

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

"""imagenes = sopa.select('img')
for i in imagenes:
    print(i)"""

imagenes = sopa.select('.couser-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)

f= open('mi:imagen.jpg','wb')
f.write(imagen_curso_1)
f.close()

