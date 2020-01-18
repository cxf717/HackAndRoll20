import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, ParseMode
from datetime import datetime
import json
import os
import requests
import logging
import random
from dbhelper import DBHelper

###### Data structures ######
#characters
characterDict = {
    "character one" : "description",
    "character two" : "description"
}




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
    chat_id = update.effective_message.chat.id

    if (chat_type == "private" or chat_type == "channel"):
            context.bot.send_message(
                chat_id = chat_id ,
                text = f'Please start the game in a group!'
            )
    elif(chat_type == "group" or chat_type == "supergroup"):
        
       # clear database
        print("start db setup")
        db.setup(chat_id)
        print("end db setup")
        db.delete_all_users(chat_id)
        print("clear database")

        #send them to a PM where we will set up!
        keyboard_callback = [[InlineKeyboardButton("Join", callback_data='1')], [InlineKeyboardButton("Assign Character", url="t.me/claire_game_test_bot")]]
        reply_markup_callback = InlineKeyboardMarkup(keyboard_callback)

         #send gif(?) and message upon starting game 
        context.bot.send_photo(
            chat_id=chat_id , 
            photo='https://images.app.goo.gl/egrpX67bikkW438y8', 
            caption = 'A new game has been started! Click join to join the game. Click assign character for your character',
            reply_markup=reply_markup_callback
        )


        #when enough characters have joined then start game
        

        #look up the chat_id for each player that has joined
        #send each of them a message with their randomyl assigned character 
        c = random.choice(list(characterDict.keys()))

        
        #game running is true 
        game = True
        while game :
            duriansCount = 0
            goodCount = 0

            #game play:
            #send message on group chat about start
            #send tunnel message
            #send command to each player for what they should do during tunnel
            #react to responses from each player on the GC
            #send message about the start of the station time and start timer and discussion time
            #End discussion
            #Send message to each person about voting
            #React to votes from each player. Needs to add it up and see who is removed.

            if(duriansCount == 0):
                #call end game method
                game = False
            
            elif(goodCount == 0):
                #call end game method
                game = False

            elif(duriansCount == 1 and goodCount == 1):
                #call end game method
                game = False
            
            else:
                #Send message about leaving and updated player list/Winner depending on if condition
                #decrease the count and remove player from db 
                print("game continues")



#join game code 
def join(update, context):
    query = update.callback_query
    chat_id = update.effective_message.chat.id

    if query.data == '1':
        if db.check_user(query.from_user.id, chat_id) == 0:
            db.add_user(query.from_user.id, query.from_user.first_name, None, 0, chat_id)
            print("user successfully added")
            context.bot.send_message(
                chat_id=chat_id,
                text=f'Yay {query.from_user.first_name} has successfully joined the game!'
            ) 
        else:
            context.bot.send_message(
                chat_id=chat_id,
                text=f'{query.from_user.first_name} is already in the game!'
            )

        usernames_list = db.get_usernames(chat_id)

        context.bot.send_message(
            chat_id=chat_id,
            text=f'{usernames_list}'
        )
    else: 
        print("error with join button")
    
    db.get_users(chat_id)
    db.get_usernames(chat_id)



######### Handlers ###########
#add a handler for /start
updater.dispatcher.add_handler(
    CommandHandler('start', start)
)

#add handler for /start_game
updater.dispatcher.add_handler(
    CommandHandler('start_game', start_game)
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
print('Bot stopped!')
