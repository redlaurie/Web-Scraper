from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.bbc.co.uk/news/world').text

soup = BeautifulSoup(source,'lxml')

article = soup.find('div', class_='gel-layout__item gel-1/1')
articleLink = article.find('a').text

print(article.prettify())
print(articleLink)