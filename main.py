import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import mock.GPIO as GPIO

from EmbeddedSystem import EmbeddedSystem


es = EmbeddedSystem()


def button_event(channel):
    print('INFO: The button has been pressed (GPIO%d).' % channel)
    # TODO


def loop():
    GPIO.add_event_detect(es.BUTTON_PIN, GPIO.FALLING, callback=button_event, bouncetime=500)
    while True:
        es.read_environment_temp_and_humidity()
        es.print_lcd("Temp: %.2f,\nHum: %.2f" % (es.environment_temp, es.humidity))
        es.check_liquid_level()
        es.check_liquid_turbidity()
        time.sleep(1)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        es.clear_lcd()
        es.turn_off_lcd_backlight()
        es.destroy()
