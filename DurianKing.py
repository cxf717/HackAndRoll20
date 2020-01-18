import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, ParseMode
from datetime import datetime
import json
import os
import requests
import logging
from dbhelper import DBHelper


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

# Setup database when bot is started
db = DBHelper()

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
        print("start db setup")
        db.delete_all_users()
        db.setup()
        print("end db setup")

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'You have started a game of Durian King. Eee, something stinks!'
        )

        keyboard = [[InlineKeyboardButton("Join Game", callback_data="1")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo="https://stickershop.line-scdn.net/stickershop/v1/product/1431176/LINEStorePC/main.png;compress=true",
            reply_markup=reply_markup
        )

#join game code 
def join(update, context):
    query = update.callback_query
    if query.data == '1':
        db.add_user(query.from_user.id, query.from_user.username, None, 0)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Yay you have successfully joined the game!'
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'{db.get_users}'
        )
    else: 
        print("error with join button")



######### Handlers ###########
#handler for /start
updater.dispatcher.add_handler(
    CommandHandler('start', start)
)

#handler for join game button
updater.dispatcher.add_handler(
    CallbackQueryHandler(join)
)




####### Running Bot #########

# Start the bot
updater.start_polling()
print('Bot started!')

# Wait for the bot to stop
updater.idle()
db.delete_all_users()
print('Deleted db')
print('Bot stopped!')