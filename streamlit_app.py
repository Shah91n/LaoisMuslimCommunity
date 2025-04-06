from datetime import datetime
import streamlit as st
from utils.handlers import fetch_prayer_times, handle_manual_refresh, get_next_prayer, get_time_until, get_hijri_time
from content.contact import display_contact_form
from content.activity import display_activities
from content.gallery import display_image_gallery
import os

# ------------------------ß--------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------------------------------
st.set_page_config(
	page_title="Laois Muslim Community",
	layout="wide",
	initial_sidebar_state="expanded",
	page_icon="🕌",
)

# get prayer times
prayer_times = fetch_prayer_times()

st.markdown("<h1 style='text-align: center;'>Laois Muslim Community of Ireland</h1>", unsafe_allow_html=True)

# Path to your background image
main_image_path = os.path.join(os.getcwd(), 'images', 'main_image.png')
	
st.markdown("<div style='text-align: center;'>مؤسسة غير ربحية تعني بالحفاظ على الهوية الإسلامية والدمج الإيجابي للمسلمين في المجتمع الأيرلندي</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>A non-profit organisation concerned with preserving Islamic identity and the positive integration of Muslims into Irish society.</div>", unsafe_allow_html=True)

# Divider for better visual separation
st.markdown("---")
# Main prayers section in the center of the page
st.markdown("<h2 style='text-align: center;'>Prayer Times</h2>", unsafe_allow_html=True)
prayer_times_table = st.container()
with prayer_times_table:
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{prayer_times.get('Fajr', 'N/A')}</div><div style='text-align: center; font-size: 1.5em;'>Fajr</div>", unsafe_allow_html=True)
    col2.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{prayer_times.get('Dhuhr', 'N/A')}</div><div style='text-align: center; font-size: 1.5em;'>Dhuhr</div>", unsafe_allow_html=True)
    col3.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{prayer_times.get('Asr', 'N/A')}</div><div style='text-align: center; font-size: 1.5em;'>Asr</div>", unsafe_allow_html=True)
    col4.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{prayer_times.get('Maghrib', 'N/A')}</div><div style='text-align: center; font-size: 1.5em;'>Maghrib</div>", unsafe_allow_html=True)
    col5.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{prayer_times.get('Isha', 'N/A')}</div><div style='text-align: center; font-size: 1.5em;'>Isha</div>", unsafe_allow_html=True)
# Divider for better visual separation
st.markdown("---")

st.markdown("##### Jummah'a (Friday) Prayer Time is always on 1:30 PM at St. Mary's Hall, Portlaoise")

st.markdown("---")

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

# Using sidebar for all content
sidebar = st.sidebar

# Top section - Date and Next Prayer
sidebar.header("Rahman Masjid")
sidebar.subheader("Portlaoise, Ireland")
sidebar.write("**Imam:** Ahmed Halawa")
sidebar.write(f"**Date:** {datetime.now().strftime('%B %d, %Y')}")
sidebar.write(f"**Hijri Date:** {get_hijri_time()}")

next_prayer, next_time = get_next_prayer(prayer_times)
sidebar.write(f"**Next Prayer:** {next_prayer} at {next_time}")
sidebar.write(f"_{get_time_until(next_time)}_")

# Refresh button right after remaining time
if sidebar.button("🔄 Time"):
	handle_manual_refresh()

# Additional times section
sidebar.divider()
sidebar.write("**Additional Info**")
display_names = {
    'Midnight': 'Midnight',
    'Firstthird': 'First Third',
    'Lastthird': 'Last Third'
}
for key, label in display_names.items():
    sidebar.write(f"**{label}:** {prayer_times.get(key, 'N/A')}")

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
