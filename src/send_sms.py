import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

def send_sms(sms_body):
  client = Client(account_sid, auth_token)

  message = client.messages \
                  .create(
                      body=sms_body,
                      from_='+15712483980',
                      to='+61431916656'
                  )

  print(message.sid)