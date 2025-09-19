import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#print(url_base.format('15'))

"""for n in range (1, 11):
    print(url_base.format(n))
"""

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


# print(sopa.select('.product_pod'))

libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)