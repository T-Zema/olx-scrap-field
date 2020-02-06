from requests import get
from bs4 import BeautifulSoup

url = 'http://www.olx.pl/oferty/q-asus-rog/'
response = get(url)
print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

print("test")
# <link rel="next" href="https://www.olx.pl/oferty/q-asus-rog/?page=2"> nastepna strona
# class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink "
linki = []
for a in html_soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])
    linki.append(a['href'])
print (len(linki))
linki_l = list(dict.fromkeys(linki))
print(len(linki_l))


new_list = [x for x in linki_l if len(x) > 76]
print(new_list)
print(len(new_list))


# item_containers = html_soup.find_all('tr', class_='wrap')
# item_containers_offer = html_soup.find_all('div', class_='offer-wrapper')
# print(type(item_containers))
# print(len(item_containers))
# print(item_containers[0])
#
# print("test2")
# print(type(item_containers_offer))
# print(len(item_containers_offer))
# print(item_containers_offer[1])