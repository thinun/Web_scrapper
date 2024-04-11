import requests
from bs4 import BeautifulSoup

base_url = 'https://www.century21.com/real-estate/atlanta-ga/LCGAATLANTA/?p='
for x in range(1, 10, 1):
    print(base_url + str(x))
    response = requests.get(base_url + str(x))
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    all = soup.find_all('div',
                        {'class': 'property-card-primary-info'})
    print(len(all))
    # for price
    price_of_one = all[0].find_all('a', class_='listing-price')[0].text.strip()

    for item in all[1:]:
        try:
            print(item.find_all('a', class_='listing-price')[0].text.strip())
        except:
            pass
        try:
            print(item.find_all('div', class_='property-address')[0].text.strip())
        except:
            pass
        try:
            print(item.find_all('div', class_='property-city')[0].text.strip())
        except:
            pass
        try:
            print(item.find_all('div', class_='property-beds')[0].text.strip())

        except:
            pass
        try:
            print(item.find_all('div', class_='property-baths')[0].text.strip())
        except:
            pass
        try:
            print(item.find_all('div', {'class': 'property-sqft'})[0].text.strip())
        except:
            pass
