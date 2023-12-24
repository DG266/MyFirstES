try:
    import RPi.GPIO as GPIO
except:
    import mock.GPIO as GPIO

from EmbeddedSystem import EmbeddedSystem
import string
import random
import time

es = EmbeddedSystem()


def button_event(channel):
    print('button_event - GPIO%d' % channel)
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    es.print_lcd(result_str)


def loop():
    GPIO.add_event_detect(es.BUTTON_PIN, GPIO.FALLING, callback=button_event, bouncetime=500)
    while True:
        pass


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        es.clear_lcd()

        es.destroy()
