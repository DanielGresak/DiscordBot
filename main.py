import requests
from datetime import datetime, timedelta, date
from discord import Webhook, RequestsWebhookAdapter
from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


def get_webhook():
    # This is what I use to send the message to discord so it arrives at the correct place.
    DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
    return Webhook.from_url(DISCORD_WEBHOOK, adapter=RequestsWebhookAdapter())


def get_today_week():
    # This is getting the date of 7 days ahead of us. This is to compare a week from now to assignments due
    today_week = datetime.today() + timedelta(days=+7)
    # This is to format the date correctly so it'll match the format from the spreadsheet
    return today_week.strftime("%d/%m/%Y")


def get_sheet_deet():
    # This is my sheety Auth and endpoint to retrieve information from the spreadsheet
    endpoint = os.getenv("SHEETY_ENDPOINT")
    # Sending an API request to SHEETY to get the data
    response = requests.get(url=endpoint).json()
    return response["sheet1"]


def get_message(assignment):
    return f"We have an assignment, {assignment['assignment']} for {assignment['module']} due on the {assignment['date']}. " \
                          f"This assignment is worth {round(assignment['percentage'] * 100)}% of the module's final grade."


def main():
    # Looping through the sheet
    sheet_details = get_sheet_deet()
    webhook = get_webhook()
    today_week = get_today_week()

    for assignment in sheet_details:
        # Checking if today's date is the same as the reminder date
        try:
            if assignment['date'] == today_week:
                # Sending message to discord.
                message = get_message(assignment)
                webhook.send(message)
        # Catch KeyErrors with spaces in sheet
        except KeyError:
            pass


main()
