import csv

def format_csv(data):
  if data:
    formatted_csv_data = data[0].split(',')
    return formatted_csv_data

def read_csv(file_name):
  with open(file_name, 'r') as status_csvf:
    csv_data = status_csvf.readlines()
  return csv_data

def write_csv(classes_list, file_name):
  with open(file_name, 'w') as status_csvf:
    writer = csv.writer(status_csvf)
    writer.writerow(classes_list)