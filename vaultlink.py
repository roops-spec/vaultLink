import streamlit as st
import os
import uuid

st.title("vaultLink")

uploaded_file = st.file_uploader("Upload your confidential document")
password = st.text_input("Set a password to protect your file", type="password")
expiry_minutes = st.slider("Link expiry time (in minutes)", 1, 60, 15)

if uploaded_file and password:
    file_id = str(uuid.uuid4())
    save_path = f"shared_docs/{file_id}_{uploaded_file.name}"
    os.makedirs("shared_docs", exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded securely!")
    st.write(f"Share this ID: `{file_id}` and password with the receiver.")
