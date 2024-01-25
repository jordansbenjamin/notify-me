import requests
from bs4 import BeautifulSoup

URL_9024 = 'https://timetable.unsw.edu.au/2024/COMP9024.html'

res = requests.get(URL_9024)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
status_data = soup.find_all('font')
# print(status_data)

parsed_status = []

for data in status_data:
  if 'Open' in data or 'Full' in data:
    parsed_status.append(data)

print(parsed_status)

# save parsed data into csv to compare previous version with updated version
# figure out time intervals (5 mins) to request page info
# if there are changes (new differs from previous) then send txt message to notify