import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from model import predict_strength
from recommender import ai_recommendation
import logging

# setup logging biar keliatan error di terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# load token dari .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if TOKEN is None:
    raise ValueError("Token Telegram tidak ditemukan! Pastikan .env berisi TELEGRAM_TOKEN=<tokenmu>")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Halo! Aku *SafePass Bot* 🔐\n\n"
        "Kirim perintah seperti ini untuk cek password:\n"
        "`/check Rahasia123!`\n\n"
        "Aku akan menilai kekuatannya dan kasih rekomendasi untuk improve password kamu😉",
        parse_mode="Markdown"
    )

# /check
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) == 0:
            await update.message.reply_text("⚠️ Gunakan format: /check <password>")
            return

        password = context.args[0]
        strength = predict_strength(password)
        recommendation = ai_recommendation(strength)

        message = (
            f"🔐 *Password:* `{password}`\n"
            f"💪 *Kekuatan:* {strength}\n\n"
            f"🤖 *Rekomendasi AI:*\n{recommendation}"
        )

        await update.message.reply_text(message, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan: {e}")
        logging.error(e)

# jalankan bot
if __name__ == '__main__':
    import time
    while True:
        try:
            app = ApplicationBuilder().token(TOKEN).build()
            app.add_handler(CommandHandler("start", start))
            app.add_handler(CommandHandler("check", check))
            app.run_polling()
        except Exception as e:
            print("Bot error:", e)
            print("Restarting in 5 seconds...")
            time.sleep(5)

