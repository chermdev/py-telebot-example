import time
import os
import telebot
from dotenv import load_dotenv
import logging


load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)


API_KEY = os.getenv('API_KEY') if os.getenv(
    'API_KEY') else os.environ.get('API_KEY')
bot = telebot.TeleBot(API_KEY)


def exec_fn(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
        print("ConnectionError - Sending again after 5 seconds!!!")
        time.sleep(5)
        fn(*args, **kwargs)


@bot.message_handler(commands=["start"])
def start(message):
    logging.info("User entered /start Hello! Send me:\n/hello\n/greet")
    exec_fn(bot.send_message, message.chat.id,
            "Hello! Send me:\n/hello\n/greet")


@bot.message_handler(commands=["greet"])
def greet(message):
    logging.info("User entered /great Hey! How you doing?")
    exec_fn(bot.reply_to, message, "Hey! How you doing?")


@bot.message_handler(commands=["hello"])
def hello(message):
    logging.info("User entered /hello Hello!")
    exec_fn(bot.send_message, message.chat.id, "Hello!")


bot.polling()
