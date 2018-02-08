import RPi.GPIO as GPIO
import time

from constants import BOUNCE_TIME


class Button:
    def __init__(self, pin: int, debounce_time: int, cb: callable):
        self.__pin = pin
        self.waiting = False
        self.cb = cb

        GPIO.setup(self.__pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.__pin, GPIO.FALLING, callback=self.__pressed, bouncetime=BOUNCE_TIME)

    def __pressed(self, button):
        self.waiting = True
        self.cb()
        self.handled_press()

    def handled_press(self):
        self.waiting = False
