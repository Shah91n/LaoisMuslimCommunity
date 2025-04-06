from datetime import datetime, timedelta
import streamlit as st
from utils.api_requests import get_prayer_data

# This below handles the fetching from the API response
def fetch_prayer_times():
    try:
        data = get_prayer_data()
        # Extract prayer times from the response
        prayer_times = data['data']['timings']
        return prayer_times
    except KeyError as e:
        print(f"KeyError occurred: {e}")
        return {}
    
# This below handle some manipulation of the API response and uttilties

# Handle the manual refresh mechanism for prayer times
def handle_manual_refresh():
    prayer_times = fetch_prayer_times()
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute
    st.session_state.last_update = (current_hour, current_minute)
    st.rerun() 

# get the next prayer time
def get_next_prayer(prayer_times):
	current_time = datetime.now().strftime("%H:%M")
	prayer_order = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

	for prayer in prayer_order:
		if prayer in prayer_times and current_time < prayer_times[prayer]:
			return prayer, prayer_times[prayer]
	return 'Fajr', prayer_times.get('Fajr', 'N/A') # Next day's Fajr

# get the time until the next prayer
def get_time_until(target_time_str):
	current_time = datetime.now()
	target_time = datetime.strptime(target_time_str, "%H:%M").replace(
		year=current_time.year,
		month=current_time.month,
		day=current_time.day
	)

	# If the prayer time has passed today, it's for tomorrow
	if target_time < current_time:
		target_time += timedelta(days=1)

	time_diff = target_time - current_time
	total_seconds = int(time_diff.total_seconds())

	hours = total_seconds // 3600
	minutes = (total_seconds % 3600) // 60
	seconds = total_seconds % 60

	return f"Inshallah next prayer in {hours:02d} hour : {minutes:02d} mins"

def get_hijri_time():
    # Get today's Hijri date from the API
    data = get_prayer_data()
    hijri = data['data']['date']['hijri']

    # Access values
    day = hijri['day']
    month_name = hijri['month']['en']
    year = hijri['year']
    weekday = hijri['weekday']['en']

    # Return formatted Hijri date string
    return f"{month_name} {day}, {year} AH"
