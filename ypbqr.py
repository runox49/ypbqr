import streamlit as st
from promptpay import qrcode
from io import BytesIO

# --- CONFIGURATION ---
MY_NAME = "MR. SOMCHAI PROMPT"
MY_PHONE = "0812345678"  # Linked to your bank
BANK_NAME = "Kasikornbank (KBank)"
ACCOUNT_NUMBER = "123-4-56789-0"

st.set_page_config(page_title="Thai QR Pay", page_icon="฿")

# UI Header
st.title("Thai QR Payment")
st.markdown(f"**Recipient:** {MY_NAME}")
st.write(f"**Bank:** {BANK_NAME}")

# Amount Input
amount = st.number_input("Amount (THB)", min_value=1.0, value=100.0, step=0.01)

# Generate QR
payload = qrcode.generate_payload(MY_PHONE, amount)
qr_img = qrcode.to_image(payload)

# Display QR
st.image(qr_img, caption="Scan to Pay", width=300)

# Action Buttons
st.download_button("💾 Save QR to Gallery", data=qrcode.to_bytes(payload), file_name="pay_me.png")

st.write("---")
st.subheader("Can't scan?")
st.code(ACCOUNT_NUMBER, language="text")
st.caption("Copy the account number above and paste it into your Bank Transfer menu.")

# Bank App Shortcuts
st.write("Open Bank App:")
cols = st.columns(4)
with cols[0]: st.link_button("K+", "kplus://")
with cols[1]: st.link_button("SCB", "scbeasy://")
with cols[2]: st.link_button("KTB", "ktbnext://")
with cols[3]: st.link_button("BBL", "bualuangkplus://")
