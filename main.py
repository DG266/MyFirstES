from EmbeddedSystem import EmbeddedSystem
import time

# I have created an instance of the EmbeddedSystem class
es = EmbeddedSystem()

while True:
    es.turn_on_led()
    time.sleep(1)
    es.turn_off_led()


es.destroy()