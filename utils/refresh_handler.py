from datetime import datetime
import streamlit as st
from utils.api_requests import fetch_prayer_times

def handle_refresh_mechanism():
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute

    if 'last_update' not in st.session_state:
        st.session_state.last_update = (current_hour, current_minute)

    # Check if 5 minutes have passed since last update
    if (current_hour != st.session_state.last_update[0] or 
        current_minute >= st.session_state.last_update[1] + 5):
        prayer_times = fetch_prayer_times()  # Refresh prayer times
        st.session_state.last_update = (current_hour, current_minute)
        return prayer_times
    return None

def handle_manual_refresh():
    prayer_times = fetch_prayer_times()
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute
    st.session_state.last_update = (current_hour, current_minute)
    st.rerun() 