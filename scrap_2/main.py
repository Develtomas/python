# from pprint import pprint
import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import lxml
import json
import csv

# url = "https://astera64.ru/katalog/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("data/index.html", "w", encoding='UTF-8') as file:
#     file.write(src)
# with open("data/index.html", encoding='UTF-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# DOM_NAME = "https://astera64.ru"
# all_category_blocks = soup.find_all(class_='sections-list__item-text-top-part')
#
# all_cat_dictionary = {}
# for block in all_category_blocks:
#     cat_node = block.find('a', class_='dark_link color-theme-target')
#     cat_name = cat_node.text
#     cat_link = cat_node.get('href')
#     if block.find('ul', class_='list-unstyled') is None:
#         all_cat_dictionary[cat_name] = DOM_NAME + cat_link
#     else:
#         all_cat_dictionary[cat_name] = {}
#         sub_cat = block.find_all('a', class_='sections-list__item-childs-item')
#         for sub in sub_cat:
#             sub_name = sub.find('span', class_='sections-list__item-childs-item-name').text
#             sub_link = sub.get('href')
#             all_cat_dictionary[cat_name][sub_name] = DOM_NAME + sub_link
# # pprint(all_cat_dictionary)
#
# with open('data/all_cat.json', 'w', encoding='UTF-8') as file:
#     json.dump(all_cat_dictionary, file, indent=4, ensure_ascii=False)

with open('data/all_cat.json', encoding='UTF-8') as file:
    all_cat = json.load(file)
    iteration = 0


def parse_dict(dicts, parent=None):
    for k, v in dicts.items():
        try:
            parse_dict(v, parent=k)
        except AttributeError:
            parse_page(k, v, parent)


def parse_page(name, page, parent):
    rep = [',', ' ', '/']
    for symbol in rep:
        if symbol in name:
            name = name.replace(symbol, '_')
        if parent is not None:
            if symbol in parent:
                parent = parent.replace(symbol, '_')

    req = requests.get(url=page, headers=headers)
    src = req.text

    with open(f'data/cat/{name}.html', 'w', encoding='UTF-8') as inner_file:
        inner_file.write(src)
    with open(f'data/cat/{name}.html', encoding='UTF-8') as inner_file:
        src = inner_file.read()

    soup = BeautifulSoup(src, 'lxml')

    # create headers
    product_name = 'Product name'
    in_stock = 'Stock availability'
    price = 'Price'

    if parent is None:
        with open(f'data/csv/{name}.csv', 'w', encoding='UTF-8', newline='') as inner_file:
            writer = csv.writer(inner_file, quoting=csv.QUOTE_ALL)
            writer.writerow((product_name, in_stock, price))
    else:
        with open(f'data/csv/{parent}-{name}.csv', 'w', encoding='UTF-8', newline='') as inner_file:
            writer = csv.writer(inner_file, quoting=csv.QUOTE_ALL)
            writer.writerow((product_name, in_stock, price))

    # collect all products
    items = soup.find_all('div', {"itemprop": "offers"})
    item_json = []

    for item in items:
        if item.find('a', class_='js-popup-title') is not None:
            item_name = item.find('a', class_='js-popup-title').find('span', recursive=False).text
        else:
            item_name = 'no name'

        if item.find('span', class_='status-icon') is not None:
            item_stock = item.find('span', class_='status-icon').get('data-value')
        else:
            item_stock = 'no information'

        if item.find('span', class_='price__new-val') is not None:
            item_price = item.find('span', class_='price__new-val').get('content')
        else:
            item_stock = 'no price'

        if parent is None:
            with open(f'data/csv/{name}.csv', 'a', encoding='UTF-8', newline='') as inner_file:
                writer = csv.writer(inner_file, quoting=csv.QUOTE_ALL)
                writer.writerow((item_name, item_stock, item_price))
        else:
            with open(f'data/csv/{parent}-{name}.csv', 'a', encoding='UTF-8', newline='') as inner_file:
                writer = csv.writer(inner_file, quoting=csv.QUOTE_ALL)
                writer.writerow((item_name, item_stock, item_price))

        # collect to json
        item_json.append(
            {
                'Title': item_name,
                'In stock': item_stock,
                'Price': item_price
            }
        )

    if parent is None:
        with open(f'data/json/{name}.json', 'a', encoding='UTF-8') as inner_file:
            json.dump(item_json, inner_file, indent=4, ensure_ascii=False)
    else:
        with open(f'data/json/{parent}-{name}.json', 'a', encoding='UTF-8') as inner_file:
            json.dump(item_json, inner_file, indent=4, ensure_ascii=False)

    # counter
    global iteration
    iteration += 1
    print(f'Iteration count: {iteration}, category: {name}, parent: {parent} ready...')
    sleep(random.randrange(2, 6))


# init
parse_dict(all_cat)
