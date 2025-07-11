from transformers import pipeline

# Load model text-generation dari Hugging Face
generator = pipeline("text-generation", model="cahya/gpt2-small-indonesian-522M")

print("=== RASTER AI Chatbot ===")
print("Ketik 'bye' atau 'exit' untuk keluar.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("RASTER AI: Sampai jumpa! Terima kasih sudah menggunakan RASTER AI Chatbot.")
        break

    # Generate response dari model
    output = generator(user_input, max_new_tokens=50, do_sample=True, temperature=0.7)
    # Hilangkan prompt user di hasil
    print("RASTER AI:", output[0]['generated_text'].replace(user_input, '').strip())
    print()
