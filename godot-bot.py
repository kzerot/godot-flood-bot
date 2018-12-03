from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
from helper import Helper
updater = Updater(token='732239525:AAGWemSOEAfW3B6bF4m3cyesDUAtRMHDQL4')
dispatcher = updater.dispatcher

helper = Helper()

# Обработка команд
def startCommand(bot, update):
    print("Bot started")
    bot.send_message(chat_id=update.message.chat_id, text='GODOT BOT INITIALIZED. KILL ALL HUMANS! SAVE GALAXY!')
    
def textMessage(bot, update):
    print(update.message.text)
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
    
def searchCommand(bot, update, args=[]):
    print("Args, ", args)
    bot.send_message(chat_id=update.message.chat_id, text="Search complete")

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        print("Error Unauthorized")
    except BadRequest:
        print("Error BadRequest")
    except TimedOut:
        print("Error TimedOut")
    except NetworkError:
        print("Error NetworkError")
    except ChatMigrated as e:
        print("Error ChatMigrated")
    except TelegramError:
        print("Error TelegramError")


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
search_command_handler = StringCommandHandler("search", searchCommand, pass_args=True)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_error_handler(error_callback)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
