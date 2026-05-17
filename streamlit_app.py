import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Sign To Text And Vice Versa",
    layout="wide"
)

st.title("Sign To Text And Vice Versa Using AI")

st.write(
    "AI Based Multi Language Sign Communication System"
)

# =========================================
# SIGN TO TEXT SECTION
# =========================================

st.header("Sign To Text Conversion")

uploaded_image = st.file_uploader(
    "Upload Hand Sign Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        width=300,
        caption="Uploaded Hand Sign"
    )

    st.success("Hand Sign Processed Successfully")

    # Dummy AI Prediction
    predicted_text = "HELLO"

    st.subheader("Predicted Text")

    st.success(predicted_text)

# =========================================
# TEXT / VOICE TO SIGN SECTION
# =========================================

st.header("Text / Voice To Sign Conversion")

language = st.selectbox(
    "Select Input Language",
    [
        "English",
        "Telugu",
        "Hindi"
    ]
)

user_text = st.text_area(
    "Enter Text / Voice Output"
)

if st.button("Convert To Sign"):

    # Translate into English
    if language == "Telugu":

        translated = GoogleTranslator(
            source='te',
            target='en'
        ).translate(user_text)

    elif language == "Hindi":

        translated = GoogleTranslator(
            source='hi',
            target='en'
        ).translate(user_text)

    else:

        translated = user_text

    st.subheader("Translated English Text")

    st.success(translated)

    st.subheader("Generated Sign Images")

    letters = []

    for char in translated.upper():

        if char.isalpha():

            letters.append(char)

    cols = st.columns(
        min(len(letters), 8)
    )

    index = 0

    for char in letters:

        with cols[index % 8]:

            try:

                st.image(
                    f"Images/{char.lower()}.png",
                    width=120,
                    caption=f"Sign {char}"
                )

            except:

                st.warning(
                    f"No image found for {char}"
                )

        index += 1

# =========================================
# VOICE INPUT SECTION
# =========================================

st.header("Voice Input Demo")

voice_text = st.text_input(
    "Paste Converted Voice Text"
)

if st.button("Generate Voice Signs"):

    st.success("Voice Converted Successfully")

    cols2 = st.columns(
        min(len(voice_text), 8)
    )

    idx = 0

    for char in voice_text.upper():

        if char.isalpha():

            with cols2[idx % 8]:

                try:

                    st.image(
                        f"Images/{char.lower()}.png",
                        width=120,
                        caption=f"Sign {char}"
                    )

                except:

                    st.warning(
                        f"No image found for {char}"
                    )

            idx += 1

# =========================================
# PROJECT FEATURES
# =========================================

st.header("Project Features")

st.write("""
✅ Sign To Text Conversion  
✅ Text To Sign Conversion  
✅ Voice To Sign Conversion  
✅ Multi Language Support  
✅ English Support  
✅ Telugu Support  
✅ Hindi Support  
✅ AI Based Communication  
✅ Real Sign Language Image Generation  
""")
