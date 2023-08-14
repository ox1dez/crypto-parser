import requests
import csv
from bs4 import BeautifulSoup as BS


r1 = requests.get("https://myfin.by/crypto-rates")
html = BS(r1.content, 'html.parser')

info = []

for el in html.select('.odd'):
    a = el.text.split()
    for i in range(len(a)):
        if '$' in a[i]:
            index = i
            break
    price = a[index]
    name = a[0]
    d = {'name' : name, 'price' : price}
    info.append(d)



for el in html.select('.even'):
    a = el.text.split()
    for i in range(len(a)):
        if '$' in a[i]:
            index = i
            break
    price = a[index]
    name = a[0]
    d = {'name': name, 'price': price}
    info.append(d)


r2 = requests.get("https://myfin.by/crypto-rates?page=2")
html = BS(r2.content, 'html.parser')

for el in html.select('.odd'):
    a = el.text.split()
    for i in range(len(a)):
        if '$' in a[i]:
            index = i
            break
    price = a[index]
    name = a[0]
    d = {'name' : name, 'price' : price}
    info.append(d)



for el in html.select('.even'):
    a = el.text.split()
    for i in range(len(a)):
        if '$' in a[i]:
            index = i
            break
    price = a[index]
    name = a[0]
    d = {'name': name, 'price': price}
    info.append(d)


csv_file = "output.csv"

with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in info:
        writer.writerow(row)

print(info)