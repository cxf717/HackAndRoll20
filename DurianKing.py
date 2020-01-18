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
from characters import characterDict



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

# Configure game settings
MINIMUM_PLAYERS = 1

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
        keyboard_callback = [[InlineKeyboardButton("Join", callback_data='1')]]
        reply_markup_callback = InlineKeyboardMarkup(keyboard_callback)

        #send gif(?) and message upon starting game 
        global start_game_msg
        start_game_msg = context.bot.send_photo(
            chat_id=chat_id, 
            photo='https://images.app.goo.gl/egrpX67bikkW438y8', 
            caption = 'A new game has been started! Click join to join the game.',
            reply_markup=reply_markup_callback
        )

def randomiser(userid_arr):
    if (True):
       player_id = random.choice(userid_arr)
    return player_id


#gameplay function
def setCharacter (update, context, chat_id):

    #have a set number of roles and randomly assign each player to one
    #send each of them a message with their randomly assigned character 
    role_arr = ["Durian King", "Old Auntie", "Stomper"] ### hardcoded currently for testing please change
    for character in role_arr:
        player_id = randomiser(db.get_userid_arr(chat_id))
        # check if player has already been assigned a role
        user_info = db.get_user_info(player_id, chat_id)
        while user_info[2] != "None":
            player_id = randomiser(db.get_userid_arr(chat_id))
            user_info = db.get_user_info(player_id, chat_id)

        #update database to add the character
        db.set_role(player_id, character, chat_id)

        context.bot.send_message(
            chat_id=player_id,
            text='You\'re the ' + f'<b>{character}</b>!',
            parse_mode=telegram.ParseMode.HTML
        )

        gamePlay(update, context, chat_id)


def gamePlay(update, context, chat_id):
    print("heyo")

    #count the characters 
    duriansCount = 0
    goodCount = 0

    game = True

    def groupChatMessage(message):
            context.bot.send_message(
                chat_id=chat_id,
                text=message,
                parse_mode=telegram.ParseMode.HTML
            )

    def privateMessage(message):
        player_id = db.get_userid_arr(chat_id)
        for user in player_id:
            context.bot.send_message(
                chat_id=user,
                text=message,
                parse_mode=telegram.ParseMode.HTML
            )

    while game  :

        #send message on group chat about start
        groupChatMessage("start message")

        #send tunnel message
        groupChatMessage("tunnel message GC")

        #send command to each player for what they should do during tunnel
        privateMessage("Private tunnel message")
        command_keyboard = [['command']]
        reply_markup_command = telegram.ReplyKeyboardMarkup(command_keyboard)
        player_id = db.get_userid_arr(chat_id)
        for user in player_id:
            context.bot.send_message(
                chat_id=user, 
                text="Do your command", 
                reply_markup=reply_markup_command)

        #react to responses from each player on the GC
        groupChatMessage("React to tunnel player messages")

        #send message about the start of the station time and start timer and discussion time
        groupChatMessage("Station time message. You have 120 seconds to discuss")
        #timer here 

        #End discussion
        groupChatMessage("Discussion time is up! Voting begins.")

        #Send message to each person about voting
        privateMessage("voting")
        custom_keyboard_vote = [['player one', 'player two']]
        reply_markup_vote = telegram.ReplyKeyboardMarkup(custom_keyboard_vote)
        player_id = db.get_userid_arr(chat_id)
        for user in player_id:
            context.bot.send_message(
                chat_id=user, 
                text="Please vote:", 
                reply_markup=reply_markup_vote)

        #React to votes from each player. Needs to add it up and see who is removed.
        groupChatMessage("result of voting:")
        #use a counting datastructure?

        if(duriansCount == 0):
            endGame(update, context, chat_id)
            game = False
        
        elif(goodCount == 0):
            endGame(update, context, chat_id)
            game = False

        elif(duriansCount == 1 and goodCount == 1):
            endGame(update, context, chat_id)
            game = False
        
        else:
            #Send message about leaving and updated player list/Winner depending on if condition
            groupChatMessage("updated players")

            #decrease the count and remove player from db 

            print("game continues")

def endGame(update, context, chat_id):

    context.bot.send_message(
        chat_id=chat_id,
        text="game over message",
        parse_mode=telegram.ParseMode.HTML
    )

    #clean DB?
    #reset all variables



#join game code 
def join(update, context):
    query = update.callback_query
    chat_id = update.effective_message.chat.id

    if query.data == '1':
        if not db.check_user(query.from_user.id, chat_id):
            db.add_user(query.from_user.id, query.from_user.first_name, "None", 0, chat_id)
            print("user successfully added")
            context.bot.send_message(
                chat_id=chat_id,
                text=f'Yay {query.from_user.first_name} has successfully joined the game!'
            ) 

            # send or update list of players
            usernames_list = db.get_usernames_list(chat_id)
        
            if (db.get_user_count(chat_id) == 1):
                global player_list_msg
                player_list_msg = context.bot.send_message(
                    chat_id=chat_id,
                    text=f'<b>Passenger List:</b>' + f'{usernames_list}',
                    parse_mode=telegram.ParseMode.HTML
                )
            else:
                context.bot.edit_message_text(
                    chat_id=chat_id, 
                    message_id=player_list_msg.message_id,
                    text=f'<b>Passenger List:</b> ' + f'{usernames_list}',
                    parse_mode=telegram.ParseMode.HTML
                )
        else:
            context.bot.send_message(
                chat_id=chat_id,
                text=f'{query.from_user.first_name} is already in the game!'
            )

        #send enough players message
        if (db.get_user_count(chat_id) >= MINIMUM_PLAYERS): ### change number of players 
            context.bot.send_message(
                    chat_id=chat_id,
                    text=f'Enough players. Game starting!'
            )
            
            # remove join button from start game message
            context.bot.edit_message_caption(
                chat_id=chat_id,
                message_id=start_game_msg.message_id,
                photo='https://images.app.goo.gl/egrpX67bikkW438y8', 
                caption = 'A new game is starting! Your roles have been assigned. Have fun!',     
            )

            #call gameplay function
            setCharacter(update, context, chat_id)

    else: 
        print("error with join button")



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
