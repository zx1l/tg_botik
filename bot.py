import telebot as tb
from google import genai
import os

key = os.environ['KEY']
bot = tb.TeleBot(key)

GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
client = genai.Client(api_key = GEMINI_API_KEY)



@bot.message_handler(commands = ['start'])
def start_message(message):
  bot.send_message(message.chat.id, 'Введите свой запрос и Gemini-3-flash ответит вам')

def gemini(message):
  print(message.text)
  response = client.models.generate_content(
      model="gemini-3-flash-preview", contents=message.text
  )
  print(response.text)
  bot.send_message(message.chat.id, response.text)
  bot.register_next_step_handler(message, gemini)

@bot.message_handler(content_types = ['text'])
def zapros(message):
  bot.register_next_step_handler(message, gemini)


bot.infinity_polling()

