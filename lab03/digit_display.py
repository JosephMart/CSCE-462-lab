import logging
from RPi import GPIO
from time import sleep

log = logging.getLogger(__name__)

class DigitDisplay:
    def __init__(self, pins):
        self.pins = pins

        GPIO.setup([val for key, val in self.pins.items()], GPIO.OUT)
        self.off()

    def count_down(self, start, end):
        for i in range(start, end - 1, -1):
            log.debug('DigitDisplay Value: {}'.format(i))
            self.display(i)
            sleep(1)

    def count_down_with_cb(self, start, end, cb):
        for i in range(start, end - 1, -1):
            log.debug('DigitDisplay Value: {}'.format(i))
            self.display(i)
            cb()
        self.off()

    def display(self, number: int):
        funcs = [self.display_0, self.display_1, self.display_2, self.display_3, self.display_4, self.display_5, self.display_6, self.display_7, self.display_8, self.display_9]
        funcs[number]()

    def off(self):
        GPIO.output([val for key, val in self.pins.items()], True)

    def display_0(self):
        on = ['a', 'b', 'c', 'd', 'e', 'f']
        off = ['g']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)

    def display_1(self):
        on = ['b', 'c']
        off = ['a', 'd', 'e', 'f', 'g']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)


    def display_2(self):
        on = ['a', 'f', 'g', 'c', 'd']
        off = ['b', 'e']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)

    def display_3(self):
        on = ['a', 'b', 'c', 'd', 'g']
        off = [ 'e', 'f']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)


    def display_4(self):
        on = ['e', 'g', 'c', 'b']
        off = ['a', 'd', 'f']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)

    def display_5(self):
        on = ['a', 'b', 'd', 'e', 'g']
        off = [ 'c', 'f']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)

    def display_6(self):
        on = ['a', 'b', 'd', 'e', 'f', 'g']
        off = ['c']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)

    def display_7(self):
        on = ['b', 'c', 'd']
        off = [ 'a', 'e', 'f', 'g']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)

    def display_8(self):
        GPIO.output([val for key, val in self.pins.items()], False)

    def display_9(self):
        on = ['b', 'c', 'd', 'e', 'g']
        off = [ 'a', 'f']
        GPIO.output([self.pins[x] for x in on], False)
        GPIO.output([self.pins[x] for x in off], True)
