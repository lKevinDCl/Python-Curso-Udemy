import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

# print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)