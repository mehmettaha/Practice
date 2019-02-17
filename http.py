import requests
import codecs
from bs4 import BeautifulSoup
f = open("html.txt","wb")
url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
soup = soup.prettify().encode("utf-8")
f.write(soup)
title = soup.find('span')
print(title)