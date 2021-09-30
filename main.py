import requests
from datetime import datetime, timedelta, date
from discord import Webhook, RequestsWebhookAdapter
from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

today = datetime.today().strftime("%d/%m/%Y")

# This is getting the date of 7 days ahead of us. This is to compare a week from now to assignments due
today_week = datetime.today() + timedelta(days=+7)
# This is to format the date correctly so it'll match the format from the spreadsheet
today_week = today_week.strftime("%d/%m/%Y")

# This is what I use to send the message to discord so it arrives at the correct place.
webhook = Webhook.from_url(DISCORD_WEBHOOK, adapter=RequestsWebhookAdapter())

# This is my sheety Auth and endpoint to retrieve information from the spreadsheet.
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

# Sending an API request to SHEETY to get the data
response = requests.get(url=f"{SHEETY_ENDPOINT}").json()
sheet_details = response["sheet1"]


# Looping through the sheet
for assignment in sheet_details:
    # Checking if today's date is the same as the reminder date
    if assignment["date"] == today_week:
        # Sending message to discord.
        message = f"We have an assignment, {assignment['assignment']} for {assignment['module']} due on the {assignment['date']}. " \
                  f"This assignment is worth {assignment['percentage'] * 100}% of the module's final grade."
        webhook.send(message)


