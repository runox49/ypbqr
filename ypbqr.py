import streamlit as st
from promptpay import qrcode

# 1. Access your secrets (Make sure these are set in Streamlit Cloud or secrets.toml)
# If testing locally without secrets, you can temporarily replace these with strings.
pp_id = st.secrets["PROMPTPAY_ID"]
name = st.secrets["ACCOUNT_NAME"]

st.title(f"Payment for {name}")

# 2. Amount Input
amount = st.number_input("Amount (THB)", min_value=1.0, value=100.0, step=0.01)

# 3. FIXED CODE PART: Generate Payload and Image
# We generate the payload first
payload = qrcode.generate_payload(pp_id, amount)

# We use to_image() to get the PIL object for st.image
qr_img = qrcode.to_image(payload)

# 4. Display the QR Image
# Note: we pass the 'qr_img' object directly here
st.image(qr_img, caption="Scan with any Thai Banking App", width=300)

# 5. Download Button using the library's built-in byte helper
qr_bytes = qrcode.to_bytes(payload)
st.download_button(
    label="💾 Save QR to Photos",
    data=qr_bytes,
    file_name="promptpay_qr.png",
    mime="image/png"
)

# 6. Bank App Shortcuts
st.write("---")
st.subheader("Open Bank App")
cols = st.columns(2)
with cols[0]:
    st.link_button("K PLUS", "kplus://")
    st.link_button("SCB EASY", "scbeasy://")
with cols[1]:
    st.link_button("Krungthai NEXT", "ktbnext://")
    st.link_button("Bualuang", "bualuangkplus://")
