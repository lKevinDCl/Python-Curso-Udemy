import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

print(url_base.format('15'))

for n in range (1, 11):
    print(url_base.format(n))
