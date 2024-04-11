import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonhow.com/')
c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all('div', {'class': 'card mb-3'})

for title in all:
    t = title.find_all('h2')[0].text
    print(t)
