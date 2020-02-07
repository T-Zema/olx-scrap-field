from requests import get
from bs4 import BeautifulSoup
import re

""" myslę żeby klucz do wyszukiwania przekazać jako parametr..."""

key = "Thinkpad T540p"
url = 'https://www.olx.pl/oferty/q-' + key
response = get(url)
# print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)


# <link rel="next" href="https://www.olx.pl/oferty/q-asus-rog/?page=2"> nastepna strona
# class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink "
linki = []
for a in html_soup.find_all('a', href=re.compile('^https://www.olx.pl/oferta')):
    print ("Found the URL:", a['href'])
    linki.append(a['href'])
print (len(linki))

""" lista linków do zbadania """

link_non_duplicate = list(dict.fromkeys(linki))

""" bałagan """
# print (link_non_duplicate)
# print(len(link_non_duplicate))
# test_linki = [x for x in linki if key in x]
# print("test")
# print(test_linki)
# new_list = [x for x in link_non_duplicate if len(x) > 76]
# print(new_list)
# print(len(new_list))
#  operacja na jednym

site = new_list[0]
# print(type(site))
print("strona internetowa:", site)

# response_sub_site = get(site)
# print ("test................")
# html_soup_sub = BeautifulSoup(response_sub_site, 'html.parser')
# # for site in new_list:
# print ("test................")
url = new_list[0]
url = 'https://www.olx.pl/oferta/laptop-asus-rog-strix-i5-gtx1050-16gb-CID99-IDDyvA2.html'
response = get(url)
print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
# print(html_soup)
type(html_soup)
title = html_soup.find('title').text # tytul w koncu lol

item_containers = html_soup.find_all('tr', class_='wrap')
item_containers_offer = html_soup.find_all('div', class_='offer-wrapper')
item_containers_desc = html_soup.find_all('div', class_='clr lheight20 large')
item_containers_tit = html_soup.find('div', class_='offer-titlebox') # może lepiej brać tutuł z tego
item_containers_price = html_soup.find('div', class_='price-label')
print("test....")
# print(item_containers_desc)
# opis przedmiotu
for e in item_containers_desc:
    print(e.text)
cena = item_containers_price.text.replace('\n', ' ').replace('\r', '').lstrip().rstrip() # bardzo wazny kod

if "Do negocjacji" in cena:
    print("prawda")
    negocjacja = "Tak"
    negocjacja_b = True
else:
    negocjacja = "Nie"
    negocjacja_b = False
    print("nieprawda")


cena_liczba = int("".join(filter(str.isdigit,cena)))
print(type(cena_liczba))
print(cena_liczba)
print(cena)
print ("test................")
test = html_soup.text.replace('\n', ' ').replace('\r', '').lstrip().rstrip()
print ("test................")
print(test)
print ("test................")
title = str(html_soup.find('h1')).replace('\n', ' ').replace('\r', '')
print(title)




# while(i<len(urls)):
#         htmlfile=urllib.urlopen(urls[i])
# print(type(str(item_containers_desc)))
titles = re.findall('<h1\b[^>]*>(.*?)</h1>', str(title))
print("wynik",titles)

print(item_containers_tit.text.replace('\n', ' ').replace('\r', '').lstrip().rstrip())

# soup = BeautifulSoup(item_containers_tit, "html.parser")
# print([link.get_text() for link in soup.select("#h1 > a")])

# print(str(item_containers_desc))
# print(item_containers[0])
#
# print("test2")
# print(type(item_containers_offer))
# print(len(item_containers_offer))
# print(item_containers_offer[1])