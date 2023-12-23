from EmbeddedSystem import EmbeddedSystem
import string
import random
import time

es = EmbeddedSystem()


def loop():
    while True:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        es.print_lcd(result_str)
        time.sleep(1)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        es.destroy()
