import streamlit as st

st.set_page_config(page_title="Sign to Text Conversion")

st.title("Sign to Text Conversion Using AI")

st.write("Upload hand sign image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image")

    st.success("Prediction Completed")

    # Demo prediction
    st.write("Detected Text: HELLO")
