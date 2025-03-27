import requests
from bs4 import BeautifulSoup

# query
URL = 'https://www.google.com/finance/quote/NVDA:NASDAQ'
html = requests.get(URL)
soup = BeautifulSoup(html.content, 'html.parser')
# find price div
price = soup.select_one('div[data-last-price]')
currentPrice = price.get('data-last-price')
print(currentPrice)