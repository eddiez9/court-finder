import yepbooking
import datetime

site = "nbc"
location_dict = {"silverwater":1, "sevenhills":2, "homebush":3}
location = location_dict["sevenhills"]
today = datetime.datetime.now()

yepbooking.pull(site, location, today)


