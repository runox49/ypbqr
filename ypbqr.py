import streamlit as st
from promptpay import qrcode
from io import BytesIO
import numpy as np
from PIL import Image

# 1. Configuration
MY_PROMPTPAY_ID = "0864182802"  # Replace with your ID
MY_NAME = "Quan** Shen"

# 2. Input Amount
amount = st.number_input("Amount (THB)", min_value=10.0, value=100.0, step=1.00)

# 3. Generate QR Payload & Image
payload = qrcode.generate_payload(MY_PROMPTPAY_ID, amount)
qr_pil_image = qrcode.to_image(payload)

# 4. Display QR (Fixed using NumPy to avoid TypeError)
st.image(np.array(qr_pil_image), caption="Scan with any Thai Bank App", width=300)

# 5. Fixed Download Button (Using BytesIO buffer)
buf = BytesIO()
qr_pil_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="💾 Save QR to Photos",
    data=byte_im,
    file_name="payment_qr.png",
    mime="image/png"
)

# 6. Mobile Deep Links
st.write("---")
st.subheader("Open Bank App")
cols = st.columns(2)
with cols[0]:
    st.link_button("K PLUS", "kplus://")
    st.link_button("SCB EASY", "scbeasy://")
with cols[1]:
    st.link_button("Krungthai NEXT", "ktbnext://")
    st.link_button("Bualuang", "bualuangkplus://")
