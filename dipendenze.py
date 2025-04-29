import urllib.request
import bs4

def naviga3(tag) :
    if tag.name == "a":
        print(tag["href"])
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga3(stag)


url = "https://www.itsturismomarche.it/"
risultato = urllib.request.urlopen(url)
theBytes = risultato.read()
text = theBytes.decode()
doc = bs4.BeautifulSoup(text)
# print(doc.prettify())

naviga3(doc)
