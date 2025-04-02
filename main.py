from telebot import TeleBot
from commands import *

# Initialize the bot with your token from .env
bot = TeleBot(config.get_bot_token())

# Register all commands
bot.message_handler(commands=('start', 'getlink', 'firstbatch', 'lastbatch', 'stats', 'restart', 'ban'))

# Start the bot
bot.polling()
