import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, ParseMode
from datetime import datetime
import json
import os
import requests
import logging


###### Bot Setup #######

# Initialise logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load bot token
with open('token.ini', 'r') as file:
    BOT_TOKEN = file.read()

# Create the bot
updater = Updater(token=BOT_TOKEN, use_context=True)






######## Main Code ###########

# Add /start code 
# Only allows the game to start if it is /start in a group
def start(update, context):
    chat_type = update.effective_message.chat.type
    if (chat_type == "private" or chat_type == "channel"):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Please start the game in a group!'
        )
    elif (chat_type == "group" or chat_type == "supergroup"):     
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'You have started a game of Durian King. Eee, something stinks!'
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Here is my second message.'
        )






######### Handlers ###########
#add a handler for /start
updater.dispatcher.add_handler(
    CommandHandler('start', start)
)





####### Running Bot #########

# Start the bot
updater.start_polling()
print('Bot started!')

# Wait for the bot to stop
updater.idle()

print('Bot stopped!')