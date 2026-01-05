
import streamlit as st
from promptpay import qrcode
from io import BytesIO
import numpy as np
from PIL import Image
from datetime import datetime, timedelta, timezone

# 1. Configuration
# Feel free to change these directly
MY_PROMPTPAY_ID = "0864182802" 
MY_NAME = "Quanxxx Shen"

st.set_page_config(page_title="Thai QR Payment", page_icon="฿")
st.title("฿ PromptPay Payment")
st.write(f"Recipient: **{MY_NAME}**")

# 2. Input
amount = st.number_input("Amount (THB)", min_value=10.0, value=100.0, step=1.00)

# 3. Generate Payload
payload = qrcode.generate_payload(MY_PROMPTPAY_ID, amount)

# 4. FIXED: Convert to RGB to solve the "All Black" issue
# This forces the background to be white and the pixels to be black
qr_pil_image = qrcode.to_image(payload).convert("RGB")

# 5. Display (Using NumPy for stability)
st.image(np.array(qr_pil_image), caption="Scan with your Bank App", width=300)

# D. Setup Timestamp for Thailand (UTC+7)
tz_thai = timezone(timedelta(hours=7))
# Result: slip_20260105_2130.png
timestamp = datetime.now(tz_thai).strftime("%d%m%y_%H%M%S") 
dynamic_filename = f"slip_{timestamp}.png"

# 6. FIXED: Download Button using BytesIO buffer
buf = BytesIO()
qr_pil_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label=f"💾 Download QR as {dynamic_filename}",
    data=byte_im,
    file_name=dynamic_filename, # Dynamic name applied here
    mime="image/png"
)

st.write("---")
st.subheader("📬 Send Payment Slip")

# Configuration - Change these to your actual details
LINE_ID = "runoxx" 
MY_EMAIL = "flintcheen@gmail.com"

col1, col2 = st.columns(2)

with col1:
    # Line Link
    line_url = f"https://line.me/ti/p/cv5Oni1o3V"
    st.link_button("💬 By LINE", line_url, use_container_width=True)

with col2:
    # Email Link with Pre-filled Subject
    # %20 is used for spaces in the URL
    subject = "Payment Slip for PromptPay"
    email_url = f"mailto:{MY_EMAIL}?subject={subject.replace(' ', '%20')}"
    st.link_button("📧 By Email", email_url, use_container_width=True)
# 7. Mobile Deep Links
#st.write("---")
#st.subheader("Open Bank App")
#cols = st.columns(2)
#with cols[0]:
#    st.link_button("K PLUS", "kplus://")
#    st.link_button("SCB EASY", "scbeasy://")
#with cols[1]:
#    st.link_button("Krungthai", "ktbnext://")
#    st.link_button("Bangkok Bank", "bualuangkplus://")
