import os
import csv
from dotenv import load_dotenv
from csv_funcs import read_csv, write_csv, format_csv
from selenium_funcs import main_selenium_process

# Might move this to its own config file
load_dotenv()

URL = os.getenv('URL')

# selenium
main_selenium_process(URL)

# save parsed data into csv to compare previous version with updated version
    
print('status_data: ', len(format_csv(read_csv('status_data.csv'))))

# NEXT STEPS:
# figure out time intervals (10 mins) to request again
# if there are changes (new differs from previous) then send txt message to notify (test txt msg first)
# figure out how to listen to multiple requests and send txt msg for each timetable
# after all is done, figure out how to run the script 24/7