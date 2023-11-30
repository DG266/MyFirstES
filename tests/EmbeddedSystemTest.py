import unittest
from EmbeddedSystem import EmbeddedSystem
import mock.GPIO as GPIO


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.es = EmbeddedSystem()

    def test_turn_on_led(self):
        self.es.turn_on_led()

        self.assertTrue(self.es.led_has_been_turned_on)

    def test_turn_off_led(self):
        self.es.turn_off_led()

        self.assertFalse(self.es.led_has_been_turned_on)
