import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text3
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
web(1,'http://www.gumtree.pl/s-wszystkie-the-reklamy/v1b0p1?q=asus+rog')