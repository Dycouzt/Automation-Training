# This script shows how web scraping works using the beautifulsoup module in python
import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Easy Exercises

first_quote = soup.find('span', class_='text')
print(first_quote.text)

quotes = soup.find_all('small', class_='author')
for quote in quotes:
    print(quote.text)

tags = soup.find_all('div', class_='tags')
for tag in tags[:5]:
    print(tag.text)

# Intermediate Exercises

