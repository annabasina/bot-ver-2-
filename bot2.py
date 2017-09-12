from telegram.ext import Updater, CommandHandler
import logging

def start_bot(bot, update):
    mytext = '''Hello, User
    Im just an average Bot and I understand only /start
    '''
    update.message.reply_text(mytext)
    print('start')



def main():
    updtr = Updater('427662093:AAG_rgSAM5cFkO7Li82-eCYcU1f10MUu8qw')
    updtr.dispatcher.add_handler(CommandHandler('start', start_bot))

    logging.basicConfig(level=logging.ERROR)
    updtr.start_polling()
    updtr.idle()

if __name__ == '__main__':
    main()