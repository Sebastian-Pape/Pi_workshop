import telepot as tp
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import RPi.GPIO as GPIO
from tele_lamp import *
from time import sleep
import sys


# get the ID of your telegram bot
def get_ID():
    try:
        with open('ID.txt', 'r') as f:
            # [:-1] to cut '\n'
            bot_ID = f.readline()[:-1]
            print('ID', bot_ID)

            if bot_ID == '\n':
                print('No ID included in ID.txt')
            else:
                print(bot_ID)
                return bot_ID
    except IOError:
          print('No file found with the name ID.txt')

def keyboard(ident):
    custom_keyboard = [[KeyboardButton(text="Lampe Grün"), KeyboardButton(text="Lampe Blau")],
                        [KeyboardButton(text="Lampe Rot"), KeyboardButton(text="Beenden")]]
    reply_markup = ReplyKeyboardMarkup(keyboard=custom_keyboard)
    piBot.sendMessage(chat_id=ident,
                 text="Lampensteuerung aktiviert", reply_markup=reply_markup)

def keyboard_strobo(ident):
    custom_keyboard = [[KeyboardButton(text="Strobo"), KeyboardButton(text="Strobo 20")],      [KeyboardButton(text="Beenden")]]
    reply_markup = ReplyKeyboardMarkup(keyboard=custom_keyboard)
    piBot.sendMessage(chat_id=ident,
                 text="Strobosteuerung aktiviert", reply_markup=reply_markup)

def keyboard_off(ident):
    piBot.sendMessage(chat_id=ident, text="Lampensteuerung deaktiviert", reply_markup=ReplyKeyboardRemove())

# starting to interact with the Bot
def texting(message):
    print(message)
    contact_id = message['chat']['id']
    contact_name = message['chat']['first_name']
    text = message['text']
    #piBot.sendMessage(contact_id, f'Hey {contact_name}!')

    if text == 'Help':

        piBot.sendMessage(contact_id, 'Hallo, auf die folgenden Kommandos höre ich: Lampe, Lampe Strobo, Setup, Clean. Viel Spaß!')

        ### Geht nur mit Python3

        #piBot.sendMessage(contact_id, f'Hey {contact_name}, auf die folgenden Kommandos höre ich: Lampe, Lampe Strobo, clean, setup. Viel Spaß!')
        pass
    if text == 'Lampe':
        GPIO.setmode(GPIO.BOARD)
        keyboard(contact_id)
    if text == 'Lampe Grün':
        lamp_gruen()
    if text == 'Lampe Blau':
        lamp_blau()
    if text == 'Lampe Rot':
        lamp_rot()
    if text == 'Lampe Strobo':
        setup()
        keyboard_strobo(contact_id)
    if text == 'Strobo 20':
        lamp_Strobo_20()
    if text == 'Strobo':
        lamp_Strobo()
    if text == 'Beenden':
        lamp_off()
        keyboard_off(contact_id)
    if text == 'Clean':
        clean()
    if text == 'Setup':
        setup()

if __name__ == '__main__':
    piBot = tp.Bot(get_ID())
    try:
        MessageLoop(piBot, texting).run_as_thread()
        print('start')
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass
