from utils.api_requests import fetch_prayer_times
from datetime import datetime
import streamlit as st

# ------------------------ß--------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------------------------------
st.set_page_config(
	page_title="Laois Muslim Community",
	layout="wide",
	initial_sidebar_state="expanded",
	page_icon="🕌",
)

st.title("Portlaoise Prayer App 🕌 Muslim Community")
st.markdown("---")

def get_next_prayer(prayer_times):
    current_time = datetime.now().strftime("%H:%M")
    prayer_order = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
    
    for prayer in prayer_order:
        if current_time < prayer_times[prayer]:
            return prayer, prayer_times[prayer]
    return 'Fajr', prayer_times['Fajr']  # If after Isha, next prayer is tomorrow's Fajr

# get prayer times
prayer_times = fetch_prayer_times()

# Top section - Date and Next Prayer
st.header("Muslim Prayer Times - Portlaoise, Ireland")
col1, col2 = st.columns(2)
with col1:
    st.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}")
with col2:
    next_prayer, next_time = get_next_prayer(prayer_times)
    st.write(f"Next Prayer: {next_prayer} at {next_time}")

# Middle section - Main prayers in horizontal layout
st.divider()
main_prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
cols = st.columns(len(main_prayers))
for i, prayer in enumerate(main_prayers):
    with cols[i]:
        st.write(f"**{prayer}**")
        st.write(prayer_times[prayer])

# Bottom section - Additional times
st.divider()
bottom_prayers = ['Midnight', 'FirstThird', 'LastThird']
cols_bottom = st.columns(len(bottom_prayers))
for i, prayer in enumerate(bottom_prayers):
    with cols_bottom[i]:
        st.write(f"**{prayer}**")
        st.write(prayer_times[prayer])