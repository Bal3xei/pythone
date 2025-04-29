import urllib.request
import bs4

# def naviga3(tag) :
#     if tag.name == "a":
#         print(tag["href"])
#     for stag in tag.contents:
#         if type(stag) == bs4.element.Tag :
#             naviga3(stag)


# url = "https://www.itsturismomarche.it/"
# risultato = urllib.request.urlopen(url)
# theBytes = risultato.read()
# text = theBytes.decode()
# doc = bs4.BeautifulSoup(text)
# # print(doc.prettify())

# naviga3(doc)

visited = []

def crawl(url, prof , visited):
    if prof == 0:
        return
    if url in visited:
        return
    visited.append(url)
    print(url)
    try:
        response = urllib.request.urlopen(url)
        theBytes = response.read()
        text = theBytes.decode()
        doc = bs4.BeautifulSoup(text, "html.parser")
    except:
        return
    for tag in doc.find_all("a"):
        href = tag.get("href")
        if href and href.startswith("http"):
            crawl(href, prof - 1, visited)

url = "https://www.itsturismomarche.it/"
# visited = []
# def crawl2(url, prof, visited):
#    if prof == 0:
#        return
#    response = urllib.request.urlopen(url)
#    doc = bs4.BeautifulSoup(response)
#    for link in doc.find_all("a"):
#        href = link.get("href")
#        if href [0:4] and href not in visited:
#            visited.append(href)
#            print(href)
#            crawl2(href, prof - 1, visited)
          
crawl(url, 2, visited)