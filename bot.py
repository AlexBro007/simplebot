import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)
def start_bot(update, bot):


	mytext = "Yo {}! Im a simple bot and I know only the command {}".format(update.message.chat.first_name, '/start')
	logging.info("User {} entered /start".format(update.message.chat.username))

	update.message.reply_text(mytext)

def chat(update, bot):
	text = update.message.text
	logging.info("user {} entered a message: ".format(update.message.chat.username))
	logging.info(text)
	update.message.reply_text(text + " че")


def main():
	updater = Updater(settings.TELEGRAM_API_KEY, use_context=True)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start_bot))
	dp.add_handler(MessageHandler(Filters.text, chat))


	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	logging.info('Bot started')
	main()
