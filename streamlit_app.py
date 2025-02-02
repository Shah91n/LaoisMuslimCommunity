from utils.api_requests import fetch_prayer_times
from datetime import datetime, timedelta
import streamlit as st
from utils.refresh_handler import handle_refresh_mechanism, handle_manual_refresh
from content.contact import display_contact_form
from content.activity import display_activities
from content.gallery import display_image_gallery

# ------------------------ß--------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------------------------------
st.set_page_config(
	page_title="Laois Muslim Community",
	layout="wide",
	initial_sidebar_state="expanded",
	page_icon="🕌",
)

# Center the title with custom CSS
st.markdown("""
                <h1 style='text-align: center;'>
                    🕌 Welcome to Laois Muslim Community of Ireland 🕌
                </h1>
            """, unsafe_allow_html=True)

# Add welcome message and Quranic verse in main page
st.markdown("""
                <div style='text-align: center; padding: 20px; margin: 20px 0; font-style: italic;'>
                    "Allah is the Light of the heavens and the earth... Light upon light.<br>
                    Allah guideth unto His light whom He will."
                </div>
                <div style='text-align: center; font-size: 0.9em; color: #666;'>
                    The Holy Quran, Sura Al-Noor, 35
                </div>
            """, unsafe_allow_html=True)

# Add welcome message and Quranic verse in main page
st.markdown("""
                <div style='text-align: center; padding: 20px; margin: 20px 0; font-style: italic;'>
				A non-profit organisation concerned with preserving Islamic identity and the positive integration 
				of Muslims into Irish society.
                </div>
                <div style='text-align: center; padding: 20px; margin: 20px 0; font-size: 0.9em; color: #666;'>
                    مؤسسة غير ربحية تعني بالحفاظ على الهوية الإسلامية والدمج الإيجابي للمسلمين في المجتمع الأيرلندي
                </div>
            """, unsafe_allow_html=True)

# After the welcome messages, add the navigation buttons
col1, col2, col3, col4 = st.columns(4)

# Create session state to track active tab if it doesn't exist
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'school'

# Navigation buttons
if col1.button('School Information', use_container_width=True, type='primary' if st.session_state.active_tab == 'school' else 'secondary'):
    st.session_state.active_tab = 'school'
if col2.button('Activities', use_container_width=True, type='primary' if st.session_state.active_tab == 'activities' else 'secondary'):
    st.session_state.active_tab = 'activities'
if col3.button('Gallery', use_container_width=True, type='primary' if st.session_state.active_tab == 'gallery' else 'secondary'):
    st.session_state.active_tab = 'gallery'
if col4.button('Contact', use_container_width=True, type='primary' if st.session_state.active_tab == 'contact' else 'secondary'):
    st.session_state.active_tab = 'contact'

# Content display based on active tab
if st.session_state.active_tab == 'school':
    st.header("School Information")

elif st.session_state.active_tab == 'activities':
	display_activities()

elif st.session_state.active_tab == 'gallery':
	display_image_gallery()

elif st.session_state.active_tab == 'contact':
    display_contact_form()

# ------------------------ß--------------------------------------------------
# Utility functions
def get_next_prayer(prayer_times):
	current_time = datetime.now().strftime("%H:%M")
	prayer_order = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

	for prayer in prayer_order:
		if prayer in prayer_times and current_time < prayer_times[prayer]:
			return prayer, prayer_times[prayer]
	return 'Fajr', prayer_times.get('Fajr', 'N/A') # Next day's Fajr

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

	return f"{hours:02d}:{minutes:02d}:{seconds:02d} remaining"

# get prayer times
prayer_times = fetch_prayer_times()
updated_times = handle_refresh_mechanism()
if updated_times:
	prayer_times = updated_times

# Using sidebar for all content
sidebar = st.sidebar

# Top section - Date and Next Prayer
sidebar.header("Prayer Times")
sidebar.subheader("📍 Portlaoise, Ireland")
sidebar.write("**Imam:** Ahmed Halawa")
sidebar.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}")

next_prayer, next_time = get_next_prayer(prayer_times)
sidebar.write(f"**Next Prayer:** {next_prayer} at {next_time}")
sidebar.write(f"_{get_time_until(next_time)}_")

# Refresh button right after remaining time
if sidebar.button("🔄 Prayer Times"):
	handle_manual_refresh()

# Main prayers section
sidebar.divider()
main_prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
for prayer in main_prayers:
	sidebar.write(f"**{prayer}:** {prayer_times.get(prayer, 'N/A')}")

# Additional times section
sidebar.divider()
sidebar.write("**Additional Times**")
additional_prayers = ['Midnight', 'Firstthird', 'Lastthird']
for prayer in additional_prayers:
	sidebar.write(f"**{prayer}:** {prayer_times.get(prayer, 'N/A')}")

# Add social media icons at the bottom of sidebar
sidebar.divider()
social_html = '''
              <div style="display: flex; justify-content: center; gap: 20px; padding: 10px;">
                  <a href="https://www.tiktok.com/@halawa611?_t=ZN-8tStGYmer14&_r=1" target="_blank" style="text-decoration: none;">
                      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 448 512">
                          <path fill="#000000" d="M448,209.91a210.06,210.06,0,0,1-122.77-39.25V349.38A162.55,162.55,0,1,1,185,188.31V278.2a74.62,74.62,0,1,0,52.23,71.18V0l88,0a121.18,121.18,0,0,0,1.86,22.17h0A122.18,122.18,0,0,0,381,102.39a121.43,121.43,0,0,0,67,20.14Z"/>
                      </svg>
                  </a>
                  <a href="https://www.youtube.com/@AHMED_HALAWA" target="_blank" style="text-decoration: none;">
                      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 576 512">
                          <path fill="#FF0000" d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"/>
                      </svg>
                  </a>
                  <a href="https://www.facebook.com/AlRahmanPortlaoise/" target="_blank" style="text-decoration: none;">
                      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 320 512">
                          <path fill="#1877F2" d="M279.14 288l14.22-92.66h-88.91V142.41c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S256.43 0 225.36 0c-73.08 0-121.15 44.38-121.15 124.72v70.62H56v92.66h48.21V496h99.89V288z"/>
                      </svg>
                  </a>
              </div>
              '''
sidebar.markdown(social_html, unsafe_allow_html=True)
