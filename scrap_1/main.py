import re
from bs4 import BeautifulSoup

with open('C:/etl1/index2.html', encoding='UTF-8') as page:
    src = page.read()

soup = BeautifulSoup(src, 'lxml')
title = soup.title

print(title.text)
let = soup.find('div', attrs={'class': 'user__city'})
print(let)
for i in let:
    print(i.text)

user_name = soup.find('div', class_ = 'user__name').find('span').text
print(user_name)
span_list = soup.find(class_='user__info').find_all('span')
for i in span_list:
    print(i.text)

social_links = soup.find(class_='social__networks').find_all('a')
for name in social_links:
    text = name.text
    link = name.get('href')
    print(f"{text}: {link}")

post_text = soup.find('div', class_='post__text').find_parent()
print(post_text)

next_elem = soup.find('div', class_='user__city').find_next().text
print(next_elem)

next_elem = soup.find('div', class_='user__city').find_next_sibling()
print(next_elem)

links = soup.find('div', class_='some__links').find_all('a')
for link in links:
    print(link['data-attr'], link.get('href'))

find_text = soup.find('a', text=re.compile('Одежда'))

find_text_all = soup.find_all(text=re.compile("[Оо]дежда"))
