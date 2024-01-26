import os
import sched
import time
from dotenv import load_dotenv
from selenium_funcs import main_selenium_process

# Might move this to its own config file
load_dotenv()

URL = os.getenv('URL')

scheduler = sched.scheduler(time.time, time.sleep)

def interval_function(sc):
  main_selenium_process(URL)
  sc.enter(interval, 1, interval_function, (sc,))

interval = 600
scheduler.enter(interval, 1, interval_function, (scheduler,))
scheduler.run()