import logging
from RPi import GPIO
from time import sleep

log = logging.getLogger(__name__)

class DigitDisplay:
    def __init__(self, pins):
        self.pins = pins

        GPIO.setup([val for key, val in self.pins.items()], GPIO.OUT)

    def count_down(self, start, end):
        for i in range(start, end - 1, -1):
            log.debug('DigitDisplay Value: {}'.format(i))
            self.val = i
            sleep(1)

    def count_down_with_cb(self, start, end, cb):
        for i in range(start, end - 1, -1):
            log.debug('DigitDisplay Value: {}'.format(i))
            self.val = i
            cb()

    def display(self, number: int):
        pass

    def off(self):
        GPIO.output([val for key, val in self.pins.items()], True)

    def display_0(self):
        on = ['a', 'b', 'c', 'd', 'e', 'f']
        off = ['g']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)



    # def display_1(self):
    #
    # def display_2(self):
    #
    # def display_3(self):
    #
    # def display_4(self):
    #
    # def display_5(self):
    #
    # def display_6(self):
    #
    # def display_7(self):
    #
    #
    # def display_8(self):
    #     GPIO.output([val for key, val in self.pins.items()], False)
    #
    # def display_9(self):
