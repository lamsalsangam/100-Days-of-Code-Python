from bs4 import BeautifulSoup
# import lxml

with open("website.html",encoding="utf8") as file:
    contents=file.read()

soup = BeautifulSoup(contents, 'html.parser')
# soup = BeautifulSoup(contents, 'lxml')



# print(soup.title) # <title>Tsuoi's Personal Site</title>
# print(soup.title.name) # title
# print(soup.title.string) # Tsuoi's Personal Site

# print(soup) # Entire html docs
# print(soup.prettify()) # Entire html docs with indent

# print(soup.a) # First <a></a> tag in doc

# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag) # All <a></a> tag in doc ## Lists

# for tag in all_anchor_tag:
#     print(tag.getText()) # Give the text that is in the anchor tag
#     print(tag.get("href")) # Gives all of the links

# heading = soup.find(name="h1", id="name")
# print(heading) # <h1 id="name">Tsuoi</h1>

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading) # <h3 class="heading">Other Pages</h3>
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))



company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)

heading=soup.select(".heading")
print(heading) # []
