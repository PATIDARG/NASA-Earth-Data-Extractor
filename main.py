import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.earthdata.nasa.gov/learn/articles/haqast-overview'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    paragraphs = soup.find_all('p')

    with open('nasa_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for paragraph in paragraphs:
            csvwriter.writerow([paragraph.text.strip()])
else:
    print(f"Data fetch karne mein kuch problem aayi. Status Code: {response.status_code}")
