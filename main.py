import telebot
import openai
import os

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
OPENROUTER_API_KEY = os.environ['OPENROUTER_API_KEY']

openai.api_key = OPENROUTER_API_KEY
openai.api_base = "https://openrouter.ai/api/v1"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response['choices'][0]['message']['content']
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка: " + str(e))

bot.polling(non_stop=True)
