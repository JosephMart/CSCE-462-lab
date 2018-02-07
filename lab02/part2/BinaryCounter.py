import logging
from RPi import GPIO
from time import sleep

from constants import BOUNCE_TIME, LOG_CONFIG

logging.basicConfig(**LOG_CONFIG)
log = logging.getLogger(__name__)

class BinaryCounter:
    def __init__(self, b1: int = -1, b2: int = -1, b3: int = -1) -> None:
        if -1 in [b1, b2, b3]:
            raise Exception('BinaryCounter: Not valid Button Values')

        self.__b1 = b1
        self.__b2 = b2
        self.__b3 = b3
        self.__buttons = [self.__b1, self.__b2, self.__b3]
        self.__value = bin(0)

        # Setup the pins as buttons
        GPIO.setup(self.__buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for b in self.__buttons:
            GPIO.add_event_detect(b, GPIO.FALLING, callback=self.__pressed, bouncetime=BOUNCE_TIME)
        log.debug('BinaryCounter Successfully Setup ')


    @property
    def value(self):
        return self.__value


    def __pressed(self, button) -> None:
        i = self.__buttons.index(button)
        old_val = self.__value
        new_val = bin_add(self.__value, bin(2 ** i))

        if int(new_val, 2) > int('0b111', 2):
            new_val = bin(0)

        log.debug('Value changed from {} to {}'.format(old_val, new_val))
        self.__value = new_val


    def __del__(self):
        GPIO.cleanup(self.__buttons)
        log.debug('BinaryCounter Successfully Cleaned Up')



def bin_add(*args):
    return bin(sum(int(x, 2) for x in args))

def UnitTests():
    from constants import BUTTON_1, BUTTON_2, BUTTON_3

    GPIO.setmode(GPIO.BCM)
    v = BinaryCounter(BUTTON_1,BUTTON_2,BUTTON_3)
    while 1:
        v.value

if __name__ == '__main__':
    UnitTests()