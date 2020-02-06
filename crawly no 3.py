from requests import get
import re
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
#print(response.text[:500])

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)


movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))
first_movie = movie_containers[0]
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
print(first_year)
print(type(first_movie))
print(first_movie.a)

print("test")
print(first_movie.h3.a)
print(first_movie.h3.a.text)
print("test 2")
test_span =  first_movie.h3.find_all('span', class_= 'lister-item-year text-muted unbold',limit = 1)
print(test_span)
first_year = first_year.text
print(first_year)
refined = re.findall(r'\d+', first_year)
print(refined)
print(type(refined[0]))
print(int(refined[0]))