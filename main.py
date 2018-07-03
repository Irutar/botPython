import time
import logging
import bot


def main():
    logging.debug('Program Started. Press Ctrl-C to abort at any time.')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')

    print('program starts in 5 seconds. Prepare your screen')
    time.sleep(5)

    bot.start()


if __name__ == '__main__':
    main()
