import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	                level=logging.INFO,
	                filename='bot_log'
	                )

def start_bot(bot, update):
	print(update)
	mytext = '''Hello, {}!
	Im just an average Bot and I understand only /start
	'''.format(update.message.chat.first_name)

	update.message.reply_text(mytext)
	print('start')

def chat(bot, update):
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)

def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)
	updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == '__main__':
	logging.info('Bot started')
	main()
