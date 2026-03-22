import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    filters,
    ContextTypes
)
TELEGRAM_TOKEN = "8660275559:AAGp1-eQkjOYMt9PJUcXDYwilxhEkgzYM5g"
GROQ_API_KEY = "import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")"

historico = {}

def perguntar_groq(user_id, mensagem):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    if user_id not in historico:
        historico[user_id] = [
            {"role": "system", "content": """Você é um assistente útil e
responde de forma clara."""}
        ]

    historico[user_id].append({"role": "user", "content": mensagem})

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": historico[user_id]
    }

    try:
        response = requests.post(url, headers=headers, json=data, 
timeout=10)
        resposta = response.json()["choices"][0]["message"]["content"]
    except:
        return "Erro ao consultar IA."

    historico[user_id].append({"role": "assistant", "content": resposta})

    if len(historico[user_id]) > 10:
        historico[user_id] = historico[user_id][-10:]

    return resposta

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
    "Olá! Eu sou seu bot com IA. "
    "Pode me enviar uma mensagem."
)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text:
        await update.message.reply_text("Envie uma mensagem de texto.")
        return

    user_message = update.message.text
    user_id = update.message.chat_id

    resposta = perguntar_groq(user_id, user_message)

    await update.message.reply_text(resposta)
git add bot.py
git commit -m "commit limpo sem api key"
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, responder))

print("Bot rodando...")
app.run_polling()
