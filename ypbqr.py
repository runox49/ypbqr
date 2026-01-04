import streamlit as st
from promptpay import qrcode

# --- DIRECT CONFIGURATION (No Secrets) ---
MY_PROMPTPAY_ID = "0864182802"  # <-- PUT YOUR PHONE OR ID HERE
MY_NAME = "Quan"

st.set_page_config(page_title="Thai QR Pay", page_icon="฿")

st.title("💸 Quick Pay")
st.write(f"Paying to: **{MY_NAME}**")

# 1. Input Amount
amount = st.number_input("Amount (THB)", min_value=1.0, value=100.0, step=0.01)

# 2. Generate Payload & Image
# This creates the EMVCo string for Thai banks
payload = qrcode.generate_payload(MY_PROMPTPAY_ID, amount)
qr_img = qrcode.to_image(payload)

# 3. Display QR
st.image(qr_img, caption="Scan with any Thai Bank App", width=300)

# 4. Mobile Utilities
st.download_button(
    label="💾 Save QR to Photos",
    data=qrcode.to_bytes(payload),
    file_name="payment_qr.png",
    mime="image/png"
)

st.write("---")
st.subheader("Launch Bank App")
cols = st.columns(2)
with cols[0]:
    st.link_button("K PLUS", "kplus://")
    st.link_button("SCB EASY", "scbeasy://")
with cols[1]:
    st.link_button("Krungthai", "ktbnext://")
    st.link_button("Bangkok Bank", "bualuangkplus://")

st.info("💡 Tip: Save the QR first, then open your bank app to scan from your gallery.")
