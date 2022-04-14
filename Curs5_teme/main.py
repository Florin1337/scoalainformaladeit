from bs4 import BeautifulSoup
import requests
import re

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
rezultat = requests.get(url)
doc = BeautifulSoup(rezultat.text, "html.parser")

movies = doc.select("td.titleColumn")

lista = []

for index in range(0, len(movies)):

    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('((.*?))', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data = {
        "movie_title": movie_title,
        "year": year,
            }
    lista.append(data)


#for movie in lista:
#   print(movie['movie_title'], '('+movie['year'] + ')')

with open('filme.txt', 'w', encoding='utf-8') as f:
     for item in lista:
         f.write("%s\n" % item)