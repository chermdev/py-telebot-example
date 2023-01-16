import os
import telebot
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY') if os.getenv(
    'API_KEY') else os.environ.get('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! Send me:\n/hello\n/greet")


@bot.message_handler(commands=["greet"])
def greet(message):
    bot.reply_to(message, "Hey! How you doing?")


@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")


bot.polling()
