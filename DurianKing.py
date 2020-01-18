import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, ParseMode
from datetime import datetime
import json
import os
import requests
import logging
import random

###### Data structures ######
characterDict = {
    "character one" : "description",
    "character two" : "description"
}
print(characterDict)




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
                text=f'Hello, Welcome to Changi Airport MRT! Type /commands for a list of commands'
            )

#handler for being added to a group
updater.dispatcher.add_handler(
    MessageHandler(Filters.status_update.new_chat_members, new_member)
)






######## Main Code ###########

# Add /start code 
#### here it should start the PM with the people that join a group 
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Welcome to Durian King'
    )


# Add /start_game code 
def start_game(update, context):

    chat_type = update.effective_message.chat.type 
    if (chat_type == "private" or chat_type == "channel"):
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'Please start the game in a group!'
            )
    elif(chat_type == "group" or chat-type == "supergroup"):
        #send them to a PM where we will set up!
        keyboard = [[InlineKeyboardButton("Join", url="t.me/claire_game_test_bot")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        #send gif(?) and message upon starting game 
        context.bot.send_photo(
            chat_id=update.effective_chat.id, 
            photo='https://images.app.goo.gl/egrpX67bikkW438y8', 
            caption = 'A new game has been started! Click join to join the game.',
            reply_markup=reply_markup
        )

        #player joined game message
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'Player Joined:'
        )


        #when enough characters have joined then start game
        #look up the chat_id for each player that has joined
        #send each of them a message with their randomyl assigned character 
        
        c = random.choice(list(characterDict.keys()))





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
