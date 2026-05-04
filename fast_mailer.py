import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- আপডেট করা জিমেইল এবং অ্যাপ পাসওয়ার্ড ---
# এখানে পাসওয়ার্ডটি স্পেস ছাড়া দেওয়া হয়েছে যাতে কোনো ত্রুটি না হয়
EMAIL_ADDRESS = "ughh41053@gmail.com"
APP_PASSWORD = "tfvlstyjanztffft" 

# ওয়েবসাইটের ব্যাকগ্রাউন্ড এবং প্রফেশনাল ডিজাইন
st.set_page_config(page_title="AF Media Mailer", page_icon="📧")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a40 100%);
        color: white;
    }
    .stButton>button {
        background-color: #00d2ff;
        color: #1e1e2f;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
    input, textarea {
        background-color: #222 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📧 AF Media Mailer - Professional")
st.write(f"Active Account: **{EMAIL_ADDRESS}**")

receiver = st.text_input("Recipient Email (যার কাছে পাঠাবেন)")
subject = st.text_input("Subject (ইমেইল এর বিষয়)")
body = st.text_area("Message (আপনার বার্তাটি লিখুন)", height=200)

if st.button("Send Email Now"):
    if not receiver or not subject or not body:
        st.error("দয়া করে সবগুলো বক্স পূরণ করুন!")
    else:
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = receiver
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_ADDRESS, receiver, text)
            server.quit()
            st.success("✅ অভিনন্দন! ইমেইলটি সফলভাবে পাঠানো হয়েছে।")
        except Exception as e:
            st.error(f"❌ সমস্যা হয়েছে: {e}")
            st.info("টিপস: নিশ্চিত করুন আপনার জিমেইলে 2-Step Verification অন করা আছে।")

st.markdown("---")
st.caption("© 2026 AF Media & CRY Digital | Dev by MD Maruf")