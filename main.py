import telebot 
bot = telebot.TeleBot('1631776934:AAG_ZI9YPU8KQ9BFPhD1DQRZ3d6WSMQEoMk')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я спам бот. Приятно познакомиться, {message.from_user.first_name}')

    @bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == '/spam':
        bot.send_message(message.from_user.id, 'Привет, отправь мне текст!')
    else:
        bot.send_message(message.from_user.id, 'Текст принял')

        bot.polling(none_stop=True)

        @bot.message_handerl(commands = ['spam'])

        	bot.send_message(message.chat.id, '%s, wait please 👍'%message.chat.username)
@bot.message_handler(commands=['back'])        	
