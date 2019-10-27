import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.myhome.ie/rentals/results?localities=1442|1444|1446|1445|1441&region=1265&types=74&maxprice=2000")
soup = BeautifulSoup(page.content, 'html.parser')
#print (soup.prettify())

home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


#listings = soup.find("div", class_="PropertyListingCard" )
#print (listings.prettify())

#price = listings.find(class_="PropertyListingCard__Price").text
#print (price)

#address = listings.find(class_="PropertyListingCard__Address").text
#print (address)

listings = soup.findAll("div", class_="PropertyListingCard" )
for listing in listings:
    entryList = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)
    home_writer.writerow(entryList)
home_file.close()


