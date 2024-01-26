from csv_funcs import read_csv, format_csv

def check_data():
  try:
    previous_data = read_csv('status_data.csv')
    new_data = read_csv('new_status_data.csv')
  except FileNotFoundError as err:
    print(err)

  if previous_data and new_data:
    print(len(format_csv(previous_data)))
    print(len(format_csv(new_data)))
    return len(format_csv(previous_data)) != len(format_csv(new_data))