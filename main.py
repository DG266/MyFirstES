try:
    import RPi.GPIO as GPIO
except:
    import mock.GPIO as GPIO

from EmbeddedSystem import EmbeddedSystem
import string
import random
import time

es = EmbeddedSystem()


def loop():
    while True:
        if GPIO.input(es.BUTTON_PIN) == GPIO.LOW:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(8))
            es.print_lcd(result_str)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        es.destroy()
