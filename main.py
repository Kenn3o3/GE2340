from typing import Text
import constants as keys
from telegram.ext import *
import responses as R
from keep_alive import keep_alive
print("Bot started...")

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")

def help_command(update, context):
    update.message.reply_text("If you need help! you should ask for it on Google!")

def handle_message(update, context):
    test = str(update.message.text).lower()
    response = R.sample_responses(test)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))    
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

keep_alive()
main()