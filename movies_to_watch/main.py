import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"
res = requests.get(url)
data = res.text

soup = BeautifulSoup(data, "html.parser")
movie_tags = soup.find_all("h3", {"class": "listicleItem_listicle-item__title__hW_Kn"})

movie_list = [movie.get_text() for movie in movie_tags]
movie_list = movie_list[::-1]

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")






