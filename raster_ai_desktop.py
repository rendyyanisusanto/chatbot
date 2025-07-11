import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Load model text-generation Bahasa Indonesia
generator = pipeline("text-generation", model="cahya/gpt2-small-indonesian-522M")

# --- Fungsi chatbot ---
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n")

    if user_input.lower() in ["bye", "exit"]:
        chat_area.insert(tk.END, "RASTER AI: Sampai jumpa! Terima kasih sudah menggunakan RASTER AI Chatbot.\n")
        chat_area.config(state='disabled')
        root.after(1000, root.destroy)  # Tutup GUI
        return

    # Generate response
    prompt = f"Jelaskan dalam bahasa Indonesia: {user_input}"
    output = generator(prompt, max_new_tokens=50, do_sample=True, temperature=0.7)
    response = output[0]['generated_text'].replace(prompt, '').strip()

    chat_area.insert(tk.END, "RASTER AI: " + response + "\n\n")
    chat_area.config(state='disabled')
    user_entry.delete(0, tk.END)
    chat_area.see(tk.END)  # Scroll ke bawah otomatis

# --- GUI setup ---
root = tk.Tk()
root.title("RASTER AI Chatbot")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20, font=("Helvetica", 10))
chat_area.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=50)
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0,10))
user_entry.focus()

send_button = tk.Button(root, text="Kirim", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))

root.mainloop()
