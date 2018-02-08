from RPi import GPIO
from time import sleep

class RGB:
    def __init__(self, red_pin: int, green_pin: int, blue_pin: int):
        assert red_pin
        assert green_pin
        assert blue_pin

        self.__red_pin = red_pin
        self.__green_pin = green_pin
        self.__blue_pin = blue_pin
        self.pins = [self.__red_pin, self.__green_pin, self.__blue_pin]

        GPIO.setup(self.pins, GPIO.OUT)
        self.off()


    def off(self):
        GPIO.output(self.pins, False)

    def red(self):
        GPIO.output([self.__green_pin, self.__blue_pin], False)
        GPIO.output(self.__red_pin, True)

    def blue(self):
        GPIO.output([self.__red_pin, self.__green_pin], False)
        GPIO.output(self.__blue_pin, True)

    def green(self):
        GPIO.output([self.__red_pin, self.__blue_pin], False)
        GPIO.output(self.__green_pin, True)

    def flash_blue(self, flashes: int):
        for i in range(0, flashes):
            self.blue()
            sleep(.5)
            self.off()
            sleep(.5)
