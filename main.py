import aladhan

import schedule
from datetime import datetime
from playsound import playsound
import time

location = aladhan.City("Leicester", "GB", "England") # Leicester, England, United Kingdom
client = aladhan.Client(location)

adhans = []

def convert_to_24hr_time(twelve_hour_time: str) -> str:
    # Remove the parentheses around AM/PM
    twelve_hour_time = twelve_hour_time.replace("(", "").replace(")", "")

    # Convert to 24-hour format using strptime and strftime
    return datetime.strptime(twelve_hour_time, "%I:%M %p").strftime("%H:%M")



def get_prayer_times_today():
    print("Fetching Prayer Times for Today...")
    prayer_times = client.get_today_times()

    for adhan in prayer_times:
        adhans.append([adhan.get_en_name(), adhan.readable_timing(show_date=False)])
    print(f"Today's Prayer Times: {adhans}")
    time.sleep(60)  # Sleep for a minute to avoid making too many requests
    return adhans

def play_adhans():
    print("Waiting for adhans...")
    while True:

        # Check if it's time to fetch the prayer times of the day again
        current_time = time.strftime("%H:%M")
        print(f"Current Time: {current_time}, Scheduled Time: {scheduled_time}")
        if current_time == scheduled_time:
            print("It's time to fetch the prayer times again...")
            break # Break out of the loop to fetch the prayer times again

        # Check if it's time to play the adhan
        for adhan in adhans:
            print(f"Current Time: {current_time}, Adhan Time: {convert_to_24hr_time(adhan[1])}")
            if current_time == convert_to_24hr_time(adhan[1]):
                print(f"Playing {adhan[0]}...")
                playsound(f"{adhan[0]}.mp3", True)
        time.sleep(60)  # Check the time every minute

# Schedule the first script
scheduled_time = "04:01"  # Set this to your specific time, e.g., 12:05 AM
schedule.every().day.at(scheduled_time).do(get_prayer_times_today)

while True:
    # Run the first script at the scheduled time
    schedule.run_pending()
    print(adhans)

    # After running the first script, run the second script
    play_adhans()
