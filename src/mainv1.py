import requests
import csv
from bs4 import BeautifulSoup

URL_9024 = 'https://timetable.unsw.edu.au/2024/COMP9024.html'

# response object
res = requests.get(URL_9024)
# soup obj
soup = BeautifulSoup(res.text, 'html.parser')

def parse_data():
  parsed_status = []
  status_data = soup.find_all('font')

  for data in status_data:
    if 'Open' in data or 'Full' in data:
      parsed_status.append(data.text)

  return parsed_status

# print(type(parsed_status))

# save parsed data into csv to compare previous version with updated version
csv_data = None;

try:
  with open('status_data.csv') as status_csvf:
    # reader = csv.reader(status_csvf)
    # csv_data.append(reader)
    csv_data = status_csvf.readlines()
except:
  with open('status_data.csv', 'w') as status_csvf:
    writer = csv.writer(status_csvf)
    writer.writerow(parse_data())

new_csv_data = None

try:
  with open('new_status_data.csv') as status_csvf:
    # reader = csv.reader(status_csvf)
    # csv_data.append(reader)
    new_csv_data = status_csvf.readlines()
except:
  with open('new_status_data.csv', 'w') as status_csvf:
    writer = csv.writer(status_csvf)
    writer.writerow(parse_data())

def format_csv(data):
  if data:
    formatted_csv_data = data[0].split(',')
    return formatted_csv_data

print(len(format_csv(csv_data)))
print(len(format_csv(new_csv_data)))

# figure out time intervals (10 mins) to request again
# if there are changes (new differs from previous) then send txt message to notify (test txt msg first)
# figure out how to listen to multiple requests and send txt msg for each timetable
# after all is done, figure out how to run the script 24/7