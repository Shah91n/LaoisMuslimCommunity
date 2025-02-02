import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email(firstname, lastname, sender_email, message):
	# Email configuration from environment variables
	gmail_user = os.getenv('GMAIL_USER')
	gmail_password = os.getenv('GMAIL_PASSWORD')
	recipient_email = os.getenv('RECIPIENT_EMAIL')

	try:
		# Create message
		msg = MIMEMultipart()
		msg['From'] = gmail_user
		msg['To'] = recipient_email
		msg['Subject'] = f"Laois Muslim Community - Contact Form: {firstname} {lastname}"

		# Improved email body formatting
		body = f"""
		        New contact form submission:
		        
		        Name:           {firstname} {lastname}
		        Sender's Email: {sender_email}
		        
		        Message:
		        -----------------
		        {message}
		        -----------------"""

		msg.attach(MIMEText(body, 'plain'))

		# Create server connection and send
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(gmail_user, gmail_password)
		text = msg.as_string()
		server.sendmail(gmail_user, recipient_email, text)
		server.quit()
		return True
	except Exception as e:
		st.error(f"Failed to send email: {str(e)}")
		return False

def display_contact_form():
	st.header("Contact Us")

	# Create two columns for form and contact info
	col1, col2 = st.columns([3, 1])

	with col1:
		# Contact Form
		with st.form("contact_form", clear_on_submit=True):
			firstname = st.text_input("First Name*")
			lastname = st.text_input("Last Name*")
			email = st.text_input("Email*")
			message = st.text_area("Message*", height=150)

			submitted = st.form_submit_button("Submit")

			if submitted:
				# Validate all required fields
				if not firstname.strip():
					st.error("Please enter your first name")
				elif not lastname.strip():
					st.error("Please enter your last name")
				elif not email.strip():
					st.error("Please enter your email")
				elif not message.strip():
					st.error("Please enter your message")
				else:
					if send_email(firstname, lastname, email, message):
						st.success("Thank you for your message! We'll get back to you soon.")
					else:
						st.error("There was an error sending your message. Please try again later.")

	with col2:
		# Contact Information
		st.markdown("""
		               ### Location
		               Masjid Ar-Rahman (Rahman house),
		            Dublin Rd, Kilminchy, Portlaoise, 
		            Co. Laois.
		                     
		               ### Contact
		               📧 sara.rasool@islamireland.ie  
		               📞 (057) 866 5253
		               """)
	# Google Maps with clickable link
	st.subheader("Our Location")
	st.markdown("[📍 View on Google Maps](https://www.google.com/maps/place/Rahman+House,+Dublin+Rd,+Kilminchy,+Portlaoise,+Co.+Laois/@53.0393873,-7.2750827,17z/data=!3m1!4b1!4m6!3m5!1s0x485d0c5354286f5b:0x7d9886ebfc16235d!8m2!3d53.0393873!4f-7.2725078!16s%2Fg%2F119v720yw?entry=ttu&g_ep=EgoyMDI1MDEyOS4xIKXMDSoASAFQAw%3D%3D)")
	
	st.components.v1.html("""
	                      	<iframe src="https://www.google.com/maps/embed?pb=!4v1738509730970!6m8!1m7!1s2wZZMPhaXRxPwyCKbgTO_w!2m2!1d53.0396244465057!2d-7.272594422651506!3f150.80282518629292!4f-15.853869475489631!5f0.9828750278062419" 
	                      			width="100%" 
	                      			height="450" 
	                      			style="border:0;" 
	                      			allowfullscreen="" 
	                      			loading="lazy" 
	                      			referrerpolicy="no-referrer-when-downgrade">
	                      	</iframe>
	                      """, height=450)

if __name__ == "__main__":
	st.set_page_config(page_title="Contact Us", layout="wide")
	display_contact_form()
