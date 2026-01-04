import streamlit as st
from promptpay import qrcode
import numpy as np # Add this import
from PIL import Image # Add this import

# 1. Configuration
MY_PROMPTPAY_ID = "0864182802" 
amount = st.number_input("Amount (THB)", min_value=1.0, value=100.0)

# 2. Generate Payload
payload = qrcode.generate_payload(MY_PROMPTPAY_ID, amount)

# 3. FIXED IMAGE PART
# Instead of just calling to_image(), we convert it to a numpy array
# This is the most "stable" way for Streamlit to render images
qr_pil_image = qrcode.to_image(payload)
qr_numpy_array = np.array(qr_pil_image) 

# 4. Display the QR
# Use the numpy array here
st.image(qr_numpy_array, caption="Scan with any Thai Bank App", width=300)

# 5. Download Button
# Keep this part as it uses bytes which works fine for downloads
st.download_button(
    label="💾 Save QR
