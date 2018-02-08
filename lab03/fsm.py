import logging
from RPi import GPIO
from time import sleep
from multiprocessing import Process

from constants import LOG_CONFIG, MAIN_LIGHT_PINS, CROSS_LIGHT_PINS, BOUNCE_TIME, BUTTON_PIN, DISPLAY_PINS
from rgb import RGB
from button import Button
from digit_display import DigitDisplay

log = logging.getLogger(__name__)

class FSM:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.main_light = RGB(**MAIN_LIGHT_PINS)
        self.cross_light = RGB(**CROSS_LIGHT_PINS)
        self.display = DigitDisplay(DISPLAY_PINS)
        self.button = Button(BUTTON_PIN, BOUNCE_TIME, self.handled_press)

        self.S1()

    def start(self):
        log.debug('FSM process starting')
        while True:
            pass

    def S1(self):
        log.info('FSM State: S1')
        self.main_light.green()
        self.cross_light.red()

    def S2(self):
        log.info('FSM State: S2')
        self.main_light.flash_blue(10)
        self.S3()

    def S3(self):
        log.info('FSM State: S3')
        self.main_light.red()
        self.cross_light.green()
        self.display.count_down(9, 5)
        self.S4()

    def S4(self):
        log.info('FSM State: S4')
        def blue_flash():
            self.cross_light.flash_blue(1)
        self.display.count_down_with_cb(4, 0, blue_flash)
        self.S1()

    def handled_press(self):
        self.S2()
