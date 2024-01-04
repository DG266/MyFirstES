import threading
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    import mock.GPIO as GPIO

from EmbeddedSystem import EmbeddedSystem


es = EmbeddedSystem()
current_screen = 0
current_screen_lock = threading.Lock()


def show_temp_and_humidity():
    es.print_lcd(f"Temp: {es.environment_temp:.2f},\nHum: {es.humidity:.2f}")


def show_liquid_level_and_turbidity():
    es.print_lcd(f"Liq. lvl: {es.is_liquid_level_good},\nNTU: {es.ntu_val:.2f}")


def update_screen():
    with current_screen_lock:
        if current_screen == 0:
            show_temp_and_humidity()
        elif current_screen == 1:
            show_liquid_level_and_turbidity()


def button_event(channel):
    global current_screen
    print('INFO: The button has been pressed (GPIO%d).' % channel)
    with current_screen_lock:
        if current_screen == 0:
            current_screen = 1
            es.clear_lcd()
            show_liquid_level_and_turbidity()
        elif current_screen == 1:
            current_screen = 0
            es.clear_lcd()
            show_temp_and_humidity()


def loop():
    global es, current_screen

    GPIO.add_event_detect(es.BUTTON_PIN, GPIO.FALLING, callback=button_event, bouncetime=500)

    while True:
        # Read all sensors
        es.read_environment_temp_and_humidity()
        es.check_liquid_level()
        es.check_liquid_turbidity()
        es.check_water_ph()

        update_screen()

        time.sleep(0.25)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        es.clear_lcd()
        es.turn_off_lcd_backlight()
        es.destroy()
