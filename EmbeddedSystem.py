try:
    import RPi.GPIO as GPIO
except:
    import mock.GPIO as GPIO

from libs.Adafruit_LCD1602 import Adafruit_CharLCD
from libs.PCF8574 import PCF8574_GPIO
import Adafruit_DHT


class EmbeddedSystem:
    BUTTON_PIN = 4
    DHT11_PIN = 26

    # Constructor
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        # DHT11 setup
        #self.dht11 = DHT(self.DHT11_PIN)
        self.dht11 = Adafruit_DHT.DHT11

        # Button setup
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # LCD setup
        self.mcp = None
        self.lcd = None
        self.initialize_lcd()

        # Other variables
        self.environment_temp = -1
        self.humidity = -1

    def read_environment_temp_and_humidity(self):
        print("INFO: Reading environment temperature and humidity...")
        self.humidity, self.environment_temp = Adafruit_DHT.read_retry(self.dht11, self.DHT11_PIN)
        print("INFO: Done!")
        print("INFO: Temp = %.2f, Hum = %.2f" % (self.environment_temp, self.humidity))


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

    def turn_off_lcd_backlight(self):
        self.mcp.output(3, 0)

    def destroy(self):
        GPIO.cleanup()
