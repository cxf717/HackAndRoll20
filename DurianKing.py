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



####### Added to group chat main code ############

# added to new group handler code
def new_member(update, context):
    for member in update.message.new_chat_members:
        if member.username == 'claire_game_test_bot':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'Hello, Welcome to Changi Airport MRT! Type/start to begin.'
            )

#handler for being added to a group
updater.dispatcher.add_handler(
    MessageHandler(Filters.status_update.new_chat_members, new_member)
)






######## Main Code ###########

# Add /start code 
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Welcome'
    )


# Add /start_game code 
def start_game(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'You have started a game of Durian King'
    )





######### Handlers ###########
#add a handler for /start
updater.dispatcher.add_handler(
    CommandHandler('start', start)
)

#add handler for /start_game
updater.dispatcher.add_handler(
    CommandHandler('start_game', start_game)
)





####### Running Bot #########

# Start the bot
updater.start_polling()
print('Bot started!')

# Wait for the bot to stop
updater.idle()

print('Bot stopped!')