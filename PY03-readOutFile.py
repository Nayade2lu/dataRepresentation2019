
from bs4 import BeautifulSoup

with open("../week02/carviewer2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#print (soup.tr)

rows = soup.findAll("tr")
#for row in rows:
    #print ("--------")
    #print(row)

for row in rows:
    
    #print("---------")
    datalist = []
    cols = row.findAll("td")
    for col in cols:
        datalist.append(col.text)
    #print(col.text)
    print (datalist)