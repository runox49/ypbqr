import streamlit as st
from promptpay import qrcode
from io import BytesIO
import numpy as np
from PIL import Image

# 1. Configuration
MY_PROMPTPAY_ID = "081XXXXXXX"  # Replace with your ID
MY_NAME = "Your Name"

st.title("Thai QR Payment")
amount = st.number_input("Amount (THB)", min_value=1.0, value=100.0, step=0.01)

# 2. Generate the Payload (The raw EMVCo string)
payload = qrcode.generate_payload(MY_PROMPTPAY_ID, amount)

# 3. Generate the Image Object
qr_pil_image = qrcode.to_image(payload)

# 4. FIXED: Display using NumPy (Stable for Streamlit)
st.image(np.array(qr_pil_image), caption=f"Pay to {MY_NAME}", width=300)

# 5. FIXED: Download Button (Manual Bytes Conversion)
# We save the PIL image into a memory buffer to get the bytes
buf = BytesIO()
qr_pil_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="💾 Save QR to Photos",
    data=byte_im,
    file_name="payment_qr.png",
    mime="image/png"
)

# 6. Bank Links
st.write("---")
st.subheader("Open Bank App")
cols = st.columns(2)
with cols[0]:
    st.link_button("K PLUS", "kplus://")
    st.link_button("SCB EASY", "scbeasy://")
with cols[1]:
    st.link_button("Krungthai", "ktbnext://")
    st.link_button("Bangkok Bank", "bualuangkplus://")
