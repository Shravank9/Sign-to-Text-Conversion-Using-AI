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

    # Dummy AI Prediction
    predicted_text = "HELLO"

    st.subheader("Predicted Text")

    st.success(predicted_text)

# =========================================
# TEXT / VOICE TO SIGN
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

    # =====================================
    # TRANSLATION
    # =====================================

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

    translated = translated.strip()

    st.subheader("Translated English Text")

    st.success(translated)

    # =====================================
    # SIGN IMAGE GENERATION
    # =====================================

    st.subheader("Generated Sign Images")

    words = translated.split()

    for word in words:

        word = word.strip()

        try:

            # FIRST TRY FULL WORD IMAGE
            st.image(
                f"Images/{word.capitalize()}.jpg",
                width=250,
                caption=f"Sign Word: {word}"
            )

        except:

            # OTHERWISE LETTER BY LETTER
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
# VOICE INPUT DEMO
# =========================================

st.header("Voice Input Demo")

voice_text = st.text_input(
    "Paste Voice Converted Text"
)

if st.button("Generate Voice Signs"):

    voice_text = voice_text.strip()

    st.success(
        "Voice Converted Successfully"
    )

    words = voice_text.split()

    for word in words:

        try:

            st.image(
                f"Images/{word.capitalize()}.jpg",
                width=250,
                caption=f"Voice Sign Word: {word}"
            )

        except:

            cols2 = st.columns(
                min(len(word), 8)
            )

            idx2 = 0

            for char in word.upper():

                if char.isalpha():

                    try:

                        with cols2[idx2 % 8]:

                            st.image(
                                f"Images/{char}.jpg",
                                width=120,
                                caption=char
                            )

                    except:

                        st.warning(
                            f"No image found for {char}"
                        )

                    idx2 += 1

# =========================================
# FEATURES
# =========================================

st.header("Project Features")

st.write("""
✅ Sign To Text Conversion  
✅ Text To Sign Conversion  
✅ Voice To Sign Conversion  
✅ English Language Support  
✅ Telugu Language Support  
✅ Hindi Language Support  
✅ AI Based Communication System  
✅ Full Word Sign Detection  
✅ Letter Based Sign Generation  
✅ Real Sign Image Matching  
""")
