import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import speech_recognition as sr
from googletrans import Translator

# Translator
translator = Translator()

IMAGE_DIRECTORY = "Images"  # Folder with English letter sign images

# Display images
def display_images(text):
    text = text.upper()
    for widget in panel.winfo_children():
        widget.destroy()

    for char in text:
        if char.isalpha():
            file_path = os.path.join(IMAGE_DIRECTORY, f"{char}.jpg")
            if os.path.isfile(file_path):
                try:
                    img = Image.open(file_path).resize((60, 60))
                    img = ImageTk.PhotoImage(img)
                    lbl = tk.Label(panel, image=img, bg="#ffffff", bd=0)
                    lbl.image = img
                    lbl.pack(side="left", padx=5)
                except Exception as e:
                    messagebox.showerror("Error", f"Image error for '{char}': {e}")

# Manual typing
def search_and_open_images():
    text = entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    detected_lang = translator.detect(text).lang
    if detected_lang != "en":
        text = translator.translate(text, src=detected_lang, dest="en").text
    display_images(text)

# Voice input
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Listening", "Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            spoken_text = recognizer.recognize_google(audio, language="hi-IN")
        except Exception as e:
            messagebox.showerror("Error", f"Speech error: {e}")
            return

    detected_lang = translator.detect(spoken_text).lang
    if detected_lang != "en":
        text = translator.translate(spoken_text, src=detected_lang, dest="en").text
    else:
        text = spoken_text

    entry.delete(0, tk.END)
    entry.insert(0, spoken_text)
    display_images(text)

# Hover effect for buttons
def on_enter(e):
    e.widget["bg"] = "#2563eb"
    e.widget["fg"] = "white"

def on_leave(e):
    e.widget["bg"] = "#3b82f6"
    e.widget["fg"] = "white"

# GUI setup
root = tk.Tk()
root.title("Multilingual Speech/Text to Sign Language")
root.geometry("950x700")
root.configure(bg="#f3f4f6")

# Title
label_title = tk.Label(root, text="Text / Voice to Sign Language",
                       font=("Helvetica", 22, "bold"), bg="#f3f4f6", fg="#111827")
label_title.pack(pady=25)

# --- Search bar container (Google-style) ---
search_frame = tk.Frame(root, bg="white", bd=1, relief="solid")
search_frame.pack(pady=10, padx=40, fill="x")

entry = tk.Entry(search_frame, font=("Helvetica", 14), bd=0, relief="flat")
entry.pack(side="left", padx=15, pady=12, fill="x", expand=True)

# Mic button inside search bar
mic_btn = tk.Button(search_frame, text="🎤", font=("Helvetica", 14),
                    bg="white", bd=0, relief="flat", cursor="hand2", command=voice_input)
mic_btn.pack(side="right", padx=15)

# Translate button
translate_button = tk.Button(root, text="Translate Text",
                             font=("Helvetica", 13, "bold"),
                             bg="#3b82f6", fg="white",
                             relief="flat", width=20, height=2,
                             command=search_and_open_images)
translate_button.pack(pady=20)

translate_button.bind("<Enter>", on_enter)
translate_button.bind("<Leave>", on_leave)

# Results panel (sign images)
result_card = tk.Frame(root, bg="white", bd=1, relief="solid")
result_card.pack(padx=30, pady=20, fill="both", expand=True)

panel = tk.Frame(result_card, bg="white")
panel.pack(pady=30)

# Footer
label_footer = tk.Label(root, text="Supports English, Hindi, and Telugu (Text & Voice)",
                        font=("Helvetica", 10), bg="#f3f4f6", fg="#6b7280")
label_footer.pack(side="bottom", pady=10)

root.mainloop()
