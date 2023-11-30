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

    def turn_on_led(self):
        GPIO.output(self.LED_PIN, GPIO.HIGH)
        print("INFO: the LED has been turned on.")

    def turn_off_led(self):
        GPIO.output(self.LED_PIN, GPIO.LOW)
        print("INFO: the LED has been turned off.")
