import telepot as tp
import telebot
import os
import numpy as np
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

def texting(message):
    print(message)



if __name__ == '__main__':
    piBot = tp.Bot(get_ID())
    try:
        MessageLoop(piBot, texting).run_as_thread()
        print('start')
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print('Ladi Da! ')
