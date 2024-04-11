import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonhow.com/')
c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all('div', {'class': 'card mb-3'})


h2 =all[0].find_all('h2')[0].text
print(h2)
