import requests
from bs4 import BeautifulSoup
import re

def get_data():
    headers = {'user-agent':'your actual User-Agent here'}
    url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    response = requests.get(url,headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.content,'html.parser')
        products = soup.find_all('article',attrs={'class':'product_pod'})

        re_titles = r'">([^<]+)</a>'
        titles = re.findall(re_titles,str(products))

        payments = []
        for product in products:
            payments += product.find('p',attrs = {'class':'price_color'})

        data = zip(titles,payments)
        return data
get_data()