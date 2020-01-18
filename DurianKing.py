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
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Hello {update.effective_message.chat.first_name}, Welcome to Singapore!'
    )




######## Delayed Messages ###########

def delayed_msg(context):
    """Send the delayed message."""
    job = context.job
    context.bot.send_message(job.context, text='Beep!')
    
def set_dis_time(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        # Add job to queue and stop current one if there is a timer already
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(delayed_msg, due, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

def skip_dis(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in context.chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Timer successfully unset!')

######### Handlers ###########
#add a handler for /start
updater.dispatcher.add_handler(
    CommandHandler('start', start)
)

updater.dispatcher.add_handler(CommandHandler(
    'set_dis_time', set_dis_time,
    pass_args=True, pass_job_queue=True,
    pass_chat_data=True))

updater.dispatcher.add_handler(CommandHandler(
    'skip_dis', skip_dis, pass_chat_data=True))





####### Running Bot #########

# Start the bot
updater.start_polling()
print('Bot started!')

# Wait for the bot to stop
updater.idle()

print('Bot stopped!')
