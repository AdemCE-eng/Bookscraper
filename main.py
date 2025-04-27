import requests
from bs4 import BeautifulSoup
import re
from datetime import date
from tabulate import tabulate
import json

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

    return False


def get_text(type,name):
    data = get_data()
    today = date.today().strftime('%d/%m/%Y')

    if data:
        with open(f'{name}.txt','w',encoding='utf-8') as f:
            f.write(f'Type: {type}\n')
            f.write(f'Date: {today}\n')
            f.write('='*48+'\n')
            table = tabulate(data,headers=['Title','Price'],tablefmt="fancy_grid")
            f.write(table)
            print('File downloaded successfully!')
    else:
        return False


def get_json(name):
    data =get_data()
    books = [{'Title':title , 'Price':price} for title,price in data ]

    if data:
        with open(f'{name}.json','w',encoding='utf-8') as f:
            json.dump(books,f,ensure_ascii=False)

get_json('gg')