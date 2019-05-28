import requests
from bs4 import BeautifulSoup
req=requests.get('https://hyo-bin.github.io/intro_python/')

html=req.text
soup = BeautifulSoup(html, 'html.parser')

my_texts = soup.select(
    'body > p'
)

for atext in my_texts:
    print(atext.text)
