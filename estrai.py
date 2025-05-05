import urllib.request
outfile = open("")
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")
import bs4
doc = bs4.BeautifulSoup(text)
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag :

        tds = tr.contents
        sup = int(tds[4].get_text().replace(".",""))
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".",""))
        sigl = tds[7].get_text()
        denEstr = tds[5].get_text()
        densitaCalc = round((resi/sup),1)
        floatden = round(float((str(denEstr).replace(".","").replace(",","."))),1)
        if densitaCalc == floatden:
            ToF= True
        else:
            ToF= False
        print(f" {sigl} {prov:25s} {resi:9d} {sup} {densitaCalc} {floatden} {ToF}")