import requests
import lxml
from bs4 import BeautifulSoup
import yagmail

sender = "XXXX@gmail.com"
receiver = "XXXX@gmail.com"
password = "XXXXXXX"

subject = "Amazon Price Change Alert"
BUY_PRICE = 149

URL = "https://www.amazon.com/dp/B08TMTJZ8L/ref=sspa_dk_detail_0?pd_rd_i=B08TMTJZ8L&pd_rd_w=TvrYd&pf_rd_p=57cbdc41-b731-4e3d-aca7-49078b13a07b&pd_rd_wg=kMe3C&pf_rd_r=KBXAVW86GRKMWYZVRHA8&pd_rd_r=0e800b9c-b8c7-41b1-b103-97b778f9a1e5&s=kitchen&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWTFKTUE1NU4yTjlWJmVuY3J5cHRlZElkPUEwNDY4OTY0MzhBT1hWOElNNEc2TiZlbmNyeXB0ZWRBZElkPUEwMTk1MzEyMjYwVEU5MFMwOVpaVCZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9"
}

response = requests.get (URL, headers=header)
website_html = response.content

soup = BeautifulSoup (website_html, "lxml")
#print(soup.prettify())

price = soup.find (name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()

if price_as_float <BUY_PRICE:
    content= f"{title} is now {price}"
    yag = yagmail.SMTP(user=sender, password=password)
    yag.send(to=receiver, subject=subject, contents=content)
    print("Email Sent!")