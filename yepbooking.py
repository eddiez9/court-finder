import requests
from datetime import datetime
from bs4 import BeautifulSoup

def check(site, location, date):
    # Combine URL
    base_url = ".yepbooking.com.au/ajax/ajax.schema.php"
    schema_url = site + base_url 

    print("Fetching:" + site + " Location:" + str(location) + " " + str(date.day) + "/" + str(date.month) + "/" + str(date.year))

    # Get schema response
    html_text = requests.get("https://" + schema_url, params={"day": date.day, "month": date.month, "year": date.year, "id_sport": location}).text

    # Parse using html5lib leniant parsing
    soup = BeautifulSoup(html_text, "html5lib")

    # Get the number of courts and their names
    lanes_table = soup.find_all("table", class_= "schemaLaneTable")

    lanes_list = []
    for item in lanes_table:
        lanes = item.find_all("span")
        for lane in lanes:
            lanes_list.append(lane.text)

    # Get the actual availabilty table
    availability_table = soup.find_all("table", class_= "schemaIndividual")

    times_list = []
    availability_list = {}

    for item in availability_table:
        rows = item.find_all("tr")
        
        # Row 2 currently has the time slots
        times = rows[1].find_all("td")
        for time in times:
            # Not currently used
            times_list.append(time.text)


        lane_count = 0
        # Row 3 and after except the last row contains availability
        for x in range(2, len(rows)-1):
            slots = rows[x].find_all("td", class_="hour")
            
            # print(lanes_list[lane_count])
            
            for slot in slots:
                # If time slot closed/booked/in the past
                if "title" in slot.attrs:
                    # We don't really care if it's closed or booked
                    continue
                    # print(slot.attrs["title"])

                # If time slot available
                else:
                    # Split by dash and grab slot start time
                    start_time = slot.contents[0].attrs["title"].split("–")
                    start_date = str(date.day) + "/" + str(date.month) + "/" + str(date.year) + " " + start_time[0]
                    
                    # Make date object
                    date_obj = datetime.strptime(start_date, "%d/%m/%Y %I:%M%p")

                    # Create dictionary of time slot -> list of available courts [Court 1, Court 2]
                    if date_obj in availability_list.keys():
                        availability_list[date_obj].append(lanes_list[lane_count])
                    else:
                        availability_list[date_obj] = [lanes_list[lane_count]]

                    # print(date_obj)
                    # print(slot.contents[0].attrs["title"])

            lane_count += 1
            # print("-----")
            
    return(availability_list)
    
                

                