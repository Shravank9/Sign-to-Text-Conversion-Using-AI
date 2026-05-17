# Sign To Text And Vice Versa Using AI

## Live Demo
🔗 https://sign-to-text-conversion-using-ai-wetnvz4byylezufjbxajlj.streamlit.app

---

## Project Overview
This project is an AI-based communication system designed to help communication between normal users and hearing/speech impaired people using Sign Language recognition and generation.

The system supports:
- Sign To Text Conversion
- Text To Sign Conversion
- Voice To Sign Conversion
- Multi-language support

---

## Features
✅ Sign To Text Conversion  
✅ Text To Sign Conversion  
✅ Voice To Sign Conversion 

---

## Live Demo Notes
The Streamlit hosted demo is designed for showcasing the project workflow and UI online.

Some advanced functionalities are limited in the cloud demo version due to Streamlit Community Cloud restrictions.

### Limited Functionalities in Demo
- Live microphone recording is not supported directly in Streamlit Cloud.
- Some multilingual Roman Telugu/Hindi translations may not perfectly convert to English.
- Sign To Text prediction currently works as a demo workflow.
- Certain AI model functionalities are simplified for cloud deployment.

For full functionality, the project should be executed locally using the original project files.

---

## Project Workflow

### 1. Sign To Text Conversion
- Upload hand sign image
- System predicts/display text output

### 2. Text To Sign Conversion
- User enters text in any language
- System internally translates it into English
- Searches matching sign language images
- Displays full word sign images if available
- Otherwise displays letter-wise sign images

### 3. Voice To Sign Conversion
- User provides voice-converted text
- System translates internally to English
- Generates corresponding sign language images

---

## Technologies Used
- Python
- Streamlit
- Deep Translator
- Artificial Intelligence
- Machine Learning
- Image Processing

---
Run Original Project Locally
Run Sign To Text Module
python app.py
Run Text/Voice To Sign Module
python app2.py
Run Streamlit Web Demo
streamlit run streamlit_app.py
