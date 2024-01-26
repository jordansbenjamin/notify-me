import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

def send_sms():
  client = Client(account_sid, auth_token)

  message = client.messages \
                  .create(
                      body="There's a new slot for class timetables, check it now!",
                      from_='+15712483980',
                      to='+61431916656'
                  )

  print(message.sid)