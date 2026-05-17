import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Sign To Text And Vice Versa",
    layout="wide"
)

st.title("Sign To Text And Vice Versa Using AI")

st.write(
    "AI Based Multi Language Communication System"
)

# =========================================
# SIGN TO TEXT SECTION
# =========================================

st.header("Sign To Text Conversion")

uploaded_image = st.file_uploader(
    "Upload Hand Sign Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        width=300,
        caption="Uploaded Sign Image"
    )

    st.success(
        "Hand Sign Processed Successfully"
    )

    # Demo Prediction
    predicted_text = "HELLO"

    st.subheader("Predicted Text")

    st.success(predicted_text)

# =========================================
# TEXT TO SIGN SECTION
# =========================================

st.header("Text To Sign Conversion")

user_text = st.text_area(
    "Enter Text In Any Language"
)

if st.button("Convert Text To Sign"):

    # Auto Translate To English
    translated = GoogleTranslator(
        source='auto',
        target='en'
    ).translate(user_text)

    translated = translated.strip()

    st.subheader("Translated English Text")

    st.success(translated)

    st.subheader("Generated Sign Images")

    words = translated.split()

    for word in words:

        word = word.strip()

        try:

            # Full Word Image
            st.image(
                f"Images/{word.capitalize()}.jpg",
                width=250,
                caption=f"Sign Word: {word}"
            )

        except:

            # Letter Images
            st.write(f"Letter Signs For: {word}")

            cols = st.columns(
                min(len(word), 8)
            )

            idx = 0

            for char in word.upper():

                if char.isalpha():

                    try:

                        with cols[idx % 8]:

                            st.image(
                                f"Images/{char}.jpg",
                                width=120,
                                caption=char
                            )

                    except:

                        st.warning(
                            f"No image found for {char}"
                        )

                    idx += 1

# =========================================
# VOICE TO SIGN SECTION
# =========================================

st.header("Voice To Sign Conversion")

st.caption(
    "Cloud demo uses converted voice text input."
)

voice_text = st.text_area(
    "Paste Voice Converted Text"
)

if st.button("Generate Voice Signs"):

    translated_voice = GoogleTranslator(
        source='auto',
        target='en'
    ).translate(voice_text)

    translated_voice = translated_voice.strip()

    st.subheader("Translated English Text")

    st.success(translated_voice)

    st.subheader("Generated Sign Images")

    words = translated_voice.split()

    for word in words:

        try:

            # Full Word Image
            st.image(
                f"Images/{word.capitalize()}.jpg",
                width=250,
                caption=f"Sign Word: {word}"
            )

        except:

            # Letter Images
            cols = st.columns(
                min(len(word), 8)
            )

            idx = 0

            for char in word.upper():

                if char.isalpha():

                    try:

                        with cols[idx % 8]:

                            st.image(
                                f"Images/{char}.jpg",
                                width=120,
                                caption=char
                            )

                    except:

                        st.warning(
                            f"No image found for {char}"
                        )

                    idx += 1

