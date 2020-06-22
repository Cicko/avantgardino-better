import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://www.avantgardino.cz/menu/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("div", class_="dennimenu")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('data/menu.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)