import requests
from datetime import datetime
from bs4 import BeautifulSoup

def pull(site, location, date):
    base_url = ".yepbooking.com.au/ajax/ajax.schema.php"
    schema_url = site + base_url 

    print("Fetching:" + site + " Location:" + str(location) + " " + str(date.day) + "/" + str(date.month) + "/" + str(date.year))

    html_text = requests.get("https://" + schema_url, params={"day": date.day, "month": date.month, "year": date.year, "id_sport": location}).text

    soup = BeautifulSoup(html_text, "html5lib")

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

        lane_count = 0
        
        for x in range(2, len(rows)-1):
            
            slots = rows[x].find_all("td", class_="hour")
            print(lanes_list[lane_count])
            lane_count += 1

            for slot in slots:
                # If time slot closed/booked/in the past
                if "title" in slot.attrs:
                    print(slot.attrs["title"])

                # If time slot available
                else:
                    print (slot.contents[0].attrs["title"])

            print("-----")
            
                

                