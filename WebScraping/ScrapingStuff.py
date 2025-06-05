# This script shows how web scraping works using the beautifulsoup module in python
import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

authors = soup.find_all('span', class_='author')
for author in authors:
    print(author.text)
