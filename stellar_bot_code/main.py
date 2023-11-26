# module
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler,Updater,CallbackContext

import data_stellar as data_system

# system
key_token = ""  
user_bot = "Stellar bot" 

if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    app.add_handler(CommandHandler('dice', data_system.roll_dice_game))
    app.add_handler(CommandHandler('start', data_system.start_command))
    app.add_handler(CommandHandler('help', data_system.help_command))
    app.add_handler(CommandHandler('gbk', data_system.gbk_game))
    app.add_handler(CommandHandler('angka', data_system.angka_genap_game))
    app.add_handler(MessageHandler(filters.TEXT, data_system.text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, data_system.photo_message))
    app.run_polling(poll_interval=1)
    app.add_handler(MessageHandler(filters.Document, data_system.document_message))
    app.add_handler(MessageHandler(filters.Sticker, data_system.sticker_message))
    app.add_error_handler(data_system.error)