import telepot as tp
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from tele_lamp import lamp_on, lamp_off, lamp_function1, lamp_function2
from time import sleep


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
                        [KeyboardButton(text="Lampe Rot"), KeyboardButton(text="Lampe aus")]]
    reply_markup = ReplyKeyboardMarkup(keyboard=custom_keyboard)
    piBot.sendMessage(chat_id=ident,
                 text="Lampensteuerung aktiviert", reply_markup=reply_markup)

def keyboard_off(ident):
    piBot.sendMessage(chat_id=ident, text="Lampensteuerung deaktiviert", reply_markup=ReplyKeyboardRemove())

# starting to interact with the Bot
def texting(message):
    print(message)
    contact_id = message['chat']['id']
    contact_name = message['chat']['first_name']
    text = message['text']
    piBot.sendMessage(contact_id, f'Hey {contact_name}!')

    if text == 'Lampe':
        piBot.sendMessage(contact_id, 'Lampe an')
        keyboard(contact_id)
        lamp()

    if text == 'Lampe an':
        lamp_on()
    if text == 'Lampe aus':
        lamp_off()
        keyboard_off(contact_id)


if __name__ == '__main__':
    piBot = tp.Bot(get_ID())
    try:
        MessageLoop(piBot, texting).run_as_thread()
        print('start')
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass
