try:
    import RPi.GPIO as GPIO
except:
    import mock.GPIO as GPIO


class EmbeddedSystem:
    LED_PIN = 12

    # Constructor
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        # LED setup
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        # This is "False" because when you load this program on the Raspberry
        # the LED is initially off
        self.led_has_been_turned_on = False

    def turn_on_led(self):
        GPIO.output(self.LED_PIN, GPIO.HIGH)
        self.led_has_been_turned_on = True
        print("INFO: the LED has been turned on.")

    def turn_off_led(self):
        GPIO.output(self.LED_PIN, GPIO.LOW)
        self.led_has_been_turned_on = False
        print("INFO: the LED has been turned off.")

    def destroy(self):
        GPIO.cleanup()
