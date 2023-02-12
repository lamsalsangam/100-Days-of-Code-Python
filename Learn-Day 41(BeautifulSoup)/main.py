import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

soup = BeautifulSoup(response,"html.parser")

movie_names=soup.find_all(name="h3", class_="title")
movies_title =[movie.getText() for movie in movie_names]
movies=movies_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")