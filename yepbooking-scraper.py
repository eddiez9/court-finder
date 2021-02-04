import requests
from datetime import datetime
from bs4 import BeautifulSoup

day = 10
month = 2
year = 2021
site = "nbc"
location_dict = {"silverwater":1, "sevenhills":2, "homebush":3}
location = location_dict["silverwater"]

base_url = ".yepbooking.com.au/ajax/ajax.schema.php"

schema_url = site + base_url 

print("Fetching:" + site + " Location:" + str(location) + " " + str(day) + "/" + str(month) + "/" + str(year))

html_text = requests.get("https://" + schema_url, params={"day": day, "month": month, "year": year, "id_sport": location}).text

soup = BeautifulSoup(html_text, "html.parser")

lanes_table = soup.find_all("table", class_= "schemaLaneTable")

lanes_list = []
for item in lanes_table:
    lanes = item.find_all("span")
    for lane in lanes:
        lanes_list.append(lane.text)

availability_table = soup.find_all("table", class_= "schemaIndividual")

times_list = []
for item in availability_table:
    rows = item.find_all("tr")
    
    times = rows[1].find_all("td")
    for time in times:
        times_list.append(time.text)

    print (times_list)

    col_width = len(times_list)
    col_count = 0
    lane_count = 0

    slots = rows[2].find_all("td", class_="hour")
    for slot in slots:
        if "title" in slot.attrs:

            if col_count == 0:
                print(lanes_list[lane_count])
                lane_count += 1

            col_count += int(slot.attrs["colspan"])
            print(slot.attrs["title"])

            if col_count == col_width:
                print("-----")
                col_count = 0