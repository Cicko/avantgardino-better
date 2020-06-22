import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://www.avantgardino.cz/menu/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find("div", class_="dennimenu")

#titles = data.find_all('h3')

print(data)

output_rows = []
for table_row in data.findAll('tr'):
	columns = table_row.findAll('td')
	output_row = []
	for column in columns:
		output_row.append(column.text)
	output_rows.append(output_row)
	output_rows.append('NEXT_TYPE')


with open('data/menu.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(output_rows)