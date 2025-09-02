import tkinter as tk
import subprocess

# ---------------- OPEN EXTERNAL APPS ---------------- #
def open_sign_to_text():
    root.destroy()
    subprocess.Popen(["python", "app.py"])

def open_text_to_sign():
    root.destroy()
    subprocess.Popen(["python", "app2.py"])

# ---------------- HOVER EFFECTS ---------------- #
def on_enter(e):
    e.widget["bg"] = "#2563eb"   # Darker blue
    e.widget["fg"] = "white"

def on_leave(e):
    e.widget["bg"] = "#3b82f6"   # Blue
    e.widget["fg"] = "white"

# ---------------- MAIN GUI ---------------- #
root = tk.Tk()
root.title("Sign Language Translator")
root.geometry("600x400")
root.configure(bg="#f3f4f6")  # Light gray background

# --- Card Frame (center white box) ---
card = tk.Frame(root, bg="white", bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=300)

# Title
label_title = tk.Label(
    card,
    text="Sign Language Translator",
    font=("Helvetica", 20, "bold"),
    bg="white",
    fg="#1e3a8a"  # Navy blue
)
label_title.pack(pady=(25, 5))

# Subtitle
label_subtitle = tk.Label(
    card,
    text="Choose a mode to continue",
    font=("Helvetica", 12),
    bg="white",
    fg="#475569"
)
label_subtitle.pack(pady=(0, 25))

# Buttons
button_sign_to_text = tk.Button(
    card,
    text="✋ Sign to Text",
    font=("Helvetica", 13, "bold"),
    bg="#3b82f6",
    fg="white",
    relief="flat",
    width=20,
    height=2,
    bd=0,
    command=open_sign_to_text
)
button_sign_to_text.pack(pady=12)
button_sign_to_text.bind("<Enter>", on_enter)
button_sign_to_text.bind("<Leave>", on_leave)

button_text_to_sign = tk.Button(
    card,
    text="⌨ Text to Sign",
    font=("Helvetica", 13, "bold"),
    bg="#3b82f6",
    fg="white",
    relief="flat",
    width=20,
    height=2,
    bd=0,
    command=open_text_to_sign
)
button_text_to_sign.pack(pady=12)
button_text_to_sign.bind("<Enter>", on_enter)
button_text_to_sign.bind("<Leave>", on_leave)

# Footer
label_footer = tk.Label(
    root,
    text="© 2025 | UI Powered by Tkinter",
    font=("Helvetica", 10),
    bg="#f3f4f6",
    fg="#6b7280"
)
label_footer.pack(side="bottom", pady=15)

# Run
root.mainloop()
