from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text
soup=BeautifulSoup(yc_webpage, "html.parser")

headings=soup.find_all(name="span", class_="titleline")
article_texts = [heading.find(name="a").getText() for heading in headings]
points = soup.find_all(name="span", class_="score")
article_points = [int(point.getText().split()[0]) for point in points]
# for heading in headings:
#     article_text=heading.getText()
#     article_texts.append(article_text)

# print(article_texts)
# max(article_points)

articles = {article_points[i]:article_texts[i] for i in range(0,len(headings))}
print(articles)
# for heading in headings:
#     print(heading.getText())