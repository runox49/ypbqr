import streamlit as st
from promptpay import qrcode
import numpy as np
from PIL import Image

# 1. Configuration
MY_PROMPTPAY_ID = "0864182802"  # Replace with your ID
MY_NAME = "Your Name"

st.title("Thai QR Payment")
amount = st.number_input("Amount (THB)", min_value=1.0, value=100.0, step=0.01)

# 2. Generate the Payload
payload = qrcode.generate_payload(MY_PROMPTPAY_ID, amount)

# 3. FIXED: Convert PIL image to NumPy array
# This prevents the "TypeError" you encountered
qr_pil_image = qrcode.to_image(payload)
qr_numpy_array = np.array(qr_pil_image)

# 4. Display the Image
st.image(qr_numpy_array, caption=f"Pay to {MY_NAME}", width=300)

# 5. Download Button
# This uses 'to_bytes' which is safe for downloads
st.download_button(
    label="💾 Save QR to Photos",
    data=qrcode.to_bytes(payload),
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
