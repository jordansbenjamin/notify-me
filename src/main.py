import os
import sched
import time
from dotenv import load_dotenv
from csv_funcs import read_csv, write_csv, format_csv
from selenium_funcs import main_selenium_process

# Might move this to its own config file
load_dotenv()

URL = os.getenv('URL')

# selenium
main_selenium_process(URL)

# save parsed data into csv to compare previous version with updated version
    
# print('status_data: ', len(format_csv(read_csv('status_data.csv'))))

# figure out time intervals (10 mins) to request again

scheduler = sched.scheduler(time.time, time.sleep)

def interval_function(sc):
  print('This func runs at an interval')

interval = 600
scheduler.enter(interval, 1, interval_function, (scheduler,))
scheduler.run()

# if there are changes (new differs from previous) then send txt message to notify (test txt msg first)

# NEXT STEPS:
# figure out how to listen to multiple requests and send txt msg for each timetable?
# after all is done, figure out how to run the script 24/7