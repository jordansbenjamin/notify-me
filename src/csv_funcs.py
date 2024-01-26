import csv

def format_csv(data):
  if data:
    formatted_csv_data = data[0].split(',')
    return formatted_csv_data

def read_csv():
  with open('status_data.csv') as status_csvf:
    csv_data = status_csvf.readlines()
  return csv_data

def write_csv(classes_list):
  with open('status_data.csv', 'w') as status_csvf:
    writer = csv.writer(status_csvf)
    writer.writerow(classes_list)