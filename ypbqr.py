
import streamlit as st
from promptpay import qrcode
from io import BytesIO
import numpy as np
from PIL import Image

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

# 6. FIXED: Download Button using BytesIO buffer
buf = BytesIO()
qr_pil_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="💾 Save QR to Photos",
    data=byte_im,
    file_name="payment_qr.png",
    mime="image/png"
)

# 7. Mobile Deep Links
st.write("---")
st.subheader("Open Bank App")
cols = st.columns(2)
with cols[0]:
    st.link_button("K PLUS", "kplus://")
    st.link_button("SCB EASY", "scbeasy://")
with cols[1]:
    st.link_button("Krungthai", "ktbnext://")
    st.link_button("Bangkok Bank", "bualuangkplus://")
