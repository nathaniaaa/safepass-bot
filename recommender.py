from transformers import pipeline

# load NLP bawaan HuggingFace
generator = pipeline("text-generation", model="distilgpt2")

def ai_recommendation(password_strength):
    if password_strength == "Weak":
        prompt = "Wah tampaknya password kamu masih lemah nih, kamu bisa improve dengan menggunakan variansi huruf besar-kecil serta menambahkan simbol/angka"
    elif password_strength == "Medium":
        prompt = "Wah sedikit lagi nih! Kamu bisa improve lagi dengan menggunakan simbol/angka ya!"
    else:
        prompt = "Wih keren! Password kamu tergolong kategori strong. Selamat yaa"

    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]
