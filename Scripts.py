from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(
	format='%(asctime)s -%(name)s - %(levelname)s - %(message)s',
	level = logging.INFO
	)
from utils import get_crypto_coin

token = "367430113:AAFd1aSnsxCakyewy-OmGnuG8iFKt55rN14"

def start(bot, update):
    text = update.message.text
    print(text)
    update.message.reply_text("Olá, Sou o BotCoin!\nTe mostrarei os valores atualizados de cada moeda!\nMe diga qual moeda quer consultar!\n.: Para Bitcoin digite: /btc :.\n.: Para BitcoinCash digite: /bch :.\n.: Para Dashcoin digite: /dash :.\n.: Para Ethereum digite: /eth:.\n.: Para Litecoin digite: /ltc :.\n.: Para Ripple digite: /xrp :.\n.: Para Monero digite: /xmr :.\n.: Para Zcash digite: /zec :.\n.: Para visualiar o valor de todas as moedas digite: /Todas_as_Moedas :. ")


def bitcoin(bot, update):
	btc_value = get_crypto_coin("btc")
	update.message.reply_text("Preço Bitcoin: ${0:.2f}".format(btc_value))

def bitcoincash(bot, update):
	bch_value = get_crypto_coin("bch")
	update.message.reply_text("Preço BitcoinCash: ${0:.2f}".format(bch_value))

def dash(bot, update):
	dash_value = get_crypto_coin("dash")
	update.message.reply_text("Preço Dashcoin: ${0:.2f}".format(dash_value))

def ethereum(bot, update):
	eth_value = get_crypto_coin("eth")
	update.message.reply_text("Preço Ethereum: ${0:.2f}".format(eth_value))

def litecoin(bot, update):
	ltc_value = get_crypto_coin("ltc")
	update.message.reply_text("Preço Litecoin: ${0:.2f}".format(ltc_value))

def ripple(bot, update):
	xrp_value = get_crypto_coin("xrp")
	update.message.reply_text("Preço Ripple: ${0:.2f}".format(xrp_value))

def monero(bot, update):
	xmr_value = get_crypto_coin("xmr")
	update.message.reply_text("Preço Monero: ${0:.2f}".format(xmr_value))

def zcash(bot, update):
	zec_value = get_crypto_coin("zec")
	update.message.reply_text("Preço Zcash: ${0:.2f}".format(zec_value))



def allcoins(bot, update):
	btc_value = get_crypto_coin("btc")
	update.message.reply_text("Preço Bitcoin: ${0:.2f}".format(btc_value))

	bch_value = get_crypto_coin("bch")
	update.message.reply_text("Preço BitcoinCash: ${0:.2f}".format(bch_value))

	dash_value = get_crypto_coin("dash")
	update.message.reply_text("Preço Dashcoin: ${0:.2f}".format(dash_value))

	eth_value = get_crypto_coin("eth")
	update.message.reply_text("Preço Ethereum: ${0:.2f}".format(eth_value))

	ltc_value = get_crypto_coin("ltc")
	update.message.reply_text("Preço Litecoin: ${0:.2f}".format(ltc_value))

	xrp_value = get_crypto_coin("xrp")
	update.message.reply_text("Preço Ripple: ${0:.2f}".format(xrp_value))

	xmr_value = get_crypto_coin("xmr")
	update.message.reply_text("Preço Monero: ${0:.2f}".format(xmr_value))

	zec_value = get_crypto_coin("zec")
	update.message.reply_text("Preço Zcash: ${0:.2f}".format(zec_value))


def ping(bot, update):
	update.message.reply_text("pong!")

def echo(bot, update):
	text = update.message.text
	update.message.reply_text(text)

def audio(bot,update):
	update.message.reply_text("Você me enviou uma mensagem de audio! Porém, não entendo, Desculpe! ")

updater = Updater(token = token)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("ping",ping))

dp.add_handler(CommandHandler("btc",bitcoin))
dp.add_handler(CommandHandler("bch",bitcoincash))
dp.add_handler(CommandHandler("dash",dash))
dp.add_handler(CommandHandler("eth",ethereum))
dp.add_handler(CommandHandler("ltc",litecoin))
dp.add_handler(CommandHandler("xrp",ripple))
dp.add_handler(CommandHandler("xmr",monero))
dp.add_handler(CommandHandler("zec",zcash))
dp.add_handler(CommandHandler("Todas_as_Moedas",allcoins))


dp.add_handler(MessageHandler(Filters.text,echo))
dp.add_handler(MessageHandler(Filters.voice,audio))

updater.start_polling()

updater.idle()
