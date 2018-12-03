from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='732239525:AAGWemSOEAfW3B6bF4m3cyesDUAtRMHDQL')
dispatcher = updater.dispatcher

# Обработка команд
def startCommand(bot, update):
    print("Bot started")
    bot.send_message(chat_id=update.message.chat_id, text='GODOT BOT INITIALIZED. KILL ALL HUMANS! SAVE GALAXY!')
    
def textMessage(bot, update):
    print(update.message.text)
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
    
    
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
