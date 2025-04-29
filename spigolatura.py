import urllib3
import bs4

def naviga(tag):
    print(tag.name.upper())
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga(stag)
    

def naviga2(tag, indent) :
    print(indent + tag.name.upper())
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga2(stag, indent + " ")


def naviga3(tag) :
    if tag.name == "a":
        print(tag["href"])
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga3(stag)


url = "https://www.itsturismomarche.it/"
risultato = urllib3.request("GET", url)
print(type(url))
print(type(risultato.data))
text = risultato.data.decode()
doc = bs4.BeautifulSoup(text)
# print(doc.prettify())

# naviga(doc)

naviga3(doc)