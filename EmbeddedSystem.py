try:
    import RPi.GPIO as GPIO
except:
    import mock.GPIO as GPIO

from libs.Adafruit_LCD1602 import Adafruit_CharLCD
from libs.PCF8574 import PCF8574_GPIO


class EmbeddedSystem:
    BUTTON_PIN = 7
    LED_PIN = 12

    # Constructor
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        # LED setup
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        self.led_has_been_turned_on = False

        # Button setup
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # LCD setup
        self.mcp = None
        self.lcd = None
        self.initialize_lcd()

    def turn_on_led(self):
        GPIO.output(self.LED_PIN, GPIO.HIGH)
        self.led_has_been_turned_on = True
        print("INFO: the LED has been turned on.")

    def turn_off_led(self):
        GPIO.output(self.LED_PIN, GPIO.LOW)
        self.led_has_been_turned_on = False
        print("INFO: the LED has been turned off.")

    def initialize_lcd(self):
        PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
        PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

        # Create PCF8574 GPIO adapter.
        try:
            self.mcp = PCF8574_GPIO(PCF8574_address)
        except:
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                print("I2C Address Error !")
                exit(1)

        # Create LCD, passing in MCP GPIO adapter.
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=self.mcp)
        self.mcp.output(3, 1)  # turn on LCD backlight
        self.lcd.begin(16, 2)  # set number of LCD lines and columns

    def print_lcd(self, message):
        self.lcd.setCursor(0, 0)
        self.lcd.message(message)

    def clear_lcd(self):
        self.lcd.clear()

    def destroy(self):
        GPIO.cleanup()
