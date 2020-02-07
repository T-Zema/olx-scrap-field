try:
    from requests import get
    from bs4 import BeautifulSoup
    import re
    import pandas as pd
    import time
    from tqdm import tqdm
    from datetime import date
except ImportError:
    pass
"""

TO DO
- zrobić scrapowanie na kolejnych stronach
- więcej analizy danych (aktualnie 0)
- dodanie daty utworzenia oferty
- przekazywanie klucza do wyszukiwania jako parametr
- enkapsulacja
- posprzatac balagan
"""



""" klucz jako parametr? """

key = "Thinkpad T540p"
url = 'https://www.olx.pl/oferty/q-' + key
response = get(url)
# print(response.text[:500])
""" scrapowanie strony głównej z podanym kluczem """
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

"""zrobić aby """
# <link rel="next" href="https://www.olx.pl/oferty/q-asus-rog/?page=2"> nastepna strona
# class="thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink "

linki = []
for a in html_soup.find_all('a', href=re.compile('^https://www.olx.pl/oferta')):
    print ("Found the URL:", a['href'])
    linki.append(a['href'])
print(len(linki))

""" lista linków do zbadania """

link_non_duplicate = list(dict.fromkeys(linki))

raw_data = {'Tytul': [], "Link": [], 'Negocjacja': [], "Cena": [], "Data_utworzenia": [], "Opis": []}
df = pd.DataFrame(raw_data)

"""testowanie progress baru"""
ilosc_linkow = len(link_non_duplicate)



""" scrapowanie ofert z glownej strony """
for oferta in tqdm(link_non_duplicate):

    time.sleep(0.5)
    url = oferta
    """weź całą stronę"""
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    """weź opis"""
    item_containers_desc = html_soup.find_all('div', class_='clr lheight20 large')

    opis_oferty = ''
    for opis in item_containers_desc:
        print(opis.text)
        opis_oferty = opis.text.lstrip().rstrip()

    """weź cenę"""
    item_containers_price = html_soup.find('div', class_='price-label')

    cena = item_containers_price.text.replace('\n', ' ').replace('\r', '').lstrip().rstrip()  # bardzo wazny kod

    if "Do negocjacji" in cena:
        print("prawda")
        negocjacja = "Tak"
        negocjacja_b = True
    else:
        negocjacja = "Nie"
        negocjacja_b = False
        print("nieprawda")

    cena_liczba = int("".join(filter(str.isdigit, cena)))
    print(type(cena_liczba))
    print(cena_liczba)
    """ tytuł """
    title = html_soup.find('h1')
    def_title = title.text.replace('\n', ' ').replace('\r', '').lstrip().rstrip()
    print(title)
    """data"""
    dzisiaj = date.today()

    raw_data['Tytul'].append(def_title)
    raw_data['Link'].append(url)
    raw_data['Cena'].append(cena_liczba)
    raw_data['Negocjacja'].append(negocjacja)
    raw_data['Data_utworzenia'].append(dzisiaj)
    raw_data['Opis'].append(opis_oferty)
    print(raw_data)
    # df = df.append(raw_data,ignore_index=True)
    df = df.from_dict(raw_data)

print(df)
df.to_excel("output.xlsx")