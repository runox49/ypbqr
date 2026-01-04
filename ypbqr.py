import streamlit as st
from promptpay import qrcode
from io import BytesIO
from PIL import Image

# Page Config for Mobile
st.set_page_config(page_title="PromptPay Checkout", page_icon="฿", layout="centered")

# Custom CSS to make buttons look better on mobile
st.markdown("""
    <style>
    div.stButton > button:first-child { width: 100%; height: 50px; border-radius: 10px; }
    .bank-header { font-weight: bold; margin-top: 20px; margin-bottom: 10px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("฿ Thai QR Payment")

# --- 1. Configuration ---
PROMPTPAY_ID = "0864182802"  # Your Phone Number or National ID

# --- 2. User Input ---
amount = st.number_input("Enter Amount (THB)", min_value=1.0, value=100.0, step=0.01)

# --- 3. Generate QR Code ---
payload = qrcode.generate_payload(PROMPTPAY_ID, amount)
# We generate the image in memory to allow downloading
qr_img = qrcode.to_image(payload)

# Buffer for Streamlit download button
buf = BytesIO()
qr_img.save(buf, format="PNG")
byte_im = buf.getvalue()

# --- 4. Display ---
st.write("---")
st.subheader(f"Total: {amount:,.2f} Baht")
st.image(qr_img, caption="Scan with any Banking App", use_container_width=True)

# --- 5. Mobile Utilities ---
st.download_button(
    label="💾 Save QR to Photos",
    data=byte_im,
    file_name="promptpay_qr.png",
    mime="image/png",
    help="Save this to your gallery to scan it inside your bank app"
)

st.markdown("<p class='bank-header'>Quick Launch Bank App</p>", unsafe_allow_html=True)

# Deep Link Buttons
col1, col2 = st.columns(2)
with col1:
    st.link_button("K PLUS (KBank)", "kplus://")
    st.link_button("SCB EASY", "scbeasy://")
with col2:
    st.link_button("Krungthai NEXT", "ktbnext://")
    st.link_button("Bualuang (BBL)", "bualuangkplus://")

st.info("💡 **Tip:** After saving the QR, open your bank app, select 'Scan', and choose the image from your gallery.")
