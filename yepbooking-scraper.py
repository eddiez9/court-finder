import requests
from datetime import datetime
from bs4 import BeautifulSoup

day = 1
month = 2
year = 2021

# Silverwater NBC
schema_url = "https://nbc.yepbooking.com.au/ajax/ajax.schema.php?day=1&month=2&year=2021&id_sport=1"
html_text = requests.get(schema_url).text

soup = BeautifulSoup(html_text, "html.parser")

lanes_table = soup.find_all("table", class_="schemaLaneTable")

for item in lanes_table:
    lanes = item.find_all("span")
    for lane in lanes:
        print lane.text

availability_table = soup.find_all("table", class_="schemaIndividual")

for item in availability_table:
    rows = item.find_all("tr")
    print rows
