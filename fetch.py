import yepbooking
import datetime

site = "nbc"
location_dict = {"silverwater":1, "sevenhills":2, "homebush":3}
location = location_dict["silverwater"]

play_duration = 2
start_datetime = datetime.datetime(2021, 2, 18, 0)
end_datetime = datetime.datetime(2021, 2, 21, 0)

nbc_avail = yepbooking.check(site, location, start_datetime)

print(nbc_avail)


