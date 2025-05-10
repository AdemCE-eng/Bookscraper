import requests
from bs4 import BeautifulSoup
import re
from datetime import date
from tabulate import tabulate
import json

headers = {'user-agent': 'your actual User-Agent here'}

def get_url(category_name):
    url = 'https://books.toscrape.com/index.html'
    response = requests.get(url,headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.content,'html.parser')
        categories_tags = soup.find('div',attrs={'class':'side_categories'})

        re_categories = r'([\w-]+)_\d+'
        categories = re.findall(re_categories,str(categories_tags))

        re_num_categorie = r'[\w-]+_(\d+)'
        num_categorie = re.findall(re_num_categorie,str(categories_tags))

        page = list(zip(categories,num_categorie))
        for name,number in page:
            if name.lower() == category_name.lower():
                url = f'https://books.toscrape.com/catalogue/category/books/{name}_{number}/index.html'
                return url
    else:
        return False

def get_data(category_name):
    url = get_url(category_name)
    if not url:
        print(f"Category '{category_name}' not found. Please try again.")
        return False
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


def get_text(category_name):
    data = get_data(category_name)
    today = date.today().strftime('%d/%m/%Y')

    if data:
        with open(f'{category_name}.txt','w',encoding='utf-8') as f:
            f.write(f'Type: {category_name}\n')
            f.write(f'Date: {today}\n')
            f.write('='*48+'\n')
            table = tabulate(data,headers=['Title','Price'],tablefmt="fancy_grid")
            f.write(table)
            print(f'Text file "{category_name}.txt" downloaded successfully!')
    else:
        print('No data found.')


def get_json(category_name):
    data =get_data(category_name)

    if data:
        books = [{'Title': title, 'Price': price} for title, price in data]
        with open(f'{category_name}.json','w',encoding='utf-8') as f:
            json.dump(books,f,ensure_ascii=False)
            print(f'JSON file "{category_name}.json" downloaded successfully!')
    else:
        print('No data found.')


def main():
    print("Welcome to Books Scraper!")
    print("Note: If the category has two words, separate them with a '-' (dash).")
    print("Example: 'science-fiction', 'historical-fiction', etc.\n")

    category = input("Enter the book category you want to scrape: ").strip()
    while not get_url(category):
        print(f"Category '{category}' not found. Please try again.")
        category = input("Enter the book category you want to scrape: ").strip()

    save_text = input("Do you want to save the results as a text file? (y/n): ").strip().lower()
    while save_text not in ('y', 'n'):
        save_text = input("Please enter 'y' or 'n': ").strip().lower()

    if save_text == 'y':
        get_text(category)

    save_json = input("Do you also want to save the results as a JSON file? (y/n): ").strip().lower()
    while save_json not in ('y', 'n'):
        save_json = input("Please enter 'y' or 'n': ").strip().lower()

    if save_json == 'y':
        get_json(category)


if __name__ == "__main__":
    main()

