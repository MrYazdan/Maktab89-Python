import requests
from bs4 import BeautifulSoup

id_lists = [
    "l-bourse",
    "l-ons",
    "l-mesghal",
    "l-geram18",
    "l-sekee",
    "l-price_dollar_rl",
    "l-oil_brent",
    "l-crypto-tether-irr",
    "l-crypto-bitcoin"
]

# content = requests.get("https://www.tgju.org").content
# soup = BeautifulSoup(content, "html.parser")

# # -> id
# . -> class

# for _id in id_lists:
#     title = "".join(_id.split("-")[1:]).title()
#     value = soup.select_one(f"#{_id} > span.info-value > span").getText()
#
#     print(title, ":", value)

f = open("vr.html", "w")
print(requests.get("https://virgool.io/@immigration/%D9%85%D9%87%D8%A7%D8%AC%D8%B1%D8%AA-%D8%A8%D8%A7-%D9%85%D8%AF%D8%B1%DA%A9-%D9%81%D9%86%DB%8C-%D8%AD%D8%B1%D9%81%D9%87-%D8%A7%DB%8C-bzedhv6iz1kw").content, file=f)

