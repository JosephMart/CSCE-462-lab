import logging
import traceback
from RPi import GPIO
from time import sleep
from multiprocessing import Process

from constants import LOG_CONFIG, MAIN_LIGHT_PINS, CROSS_LIGHT_PINS, BOUNCE_TIME, BUTTON_PIN, DISPLAY_PINS
from rgb import RGB
from button import Button
from digit_display import DigitDisplay

logging.basicConfig(**LOG_CONFIG)
log = logging.getLogger(__name__)

def main():
    try:
        # GPIO.setmode(GPIO.BCM)

        log.debug('main Successfully Setup')
        display_tests()

    except KeyboardInterrupt:
        log.debug('User ended the program')

    except Exception as e:
        var = traceback.format_exc()
        log.debug(e)
        log.debug(str(var))

    finally:
        GPIO.cleanup()
        log.debug('Main Cleaned Up')

def button_tests():
    def cb():
        log.debug('Entered Button cb')
        sleep(5)
        log.debug('Exiting Button cb')
    button = Button(BUTTON_PIN, BOUNCE_TIME, cb)

    while True:
        pass

def main_light_tests():
    main_light = RGB(**MAIN_LIGHT_PINS)
    log.debug('main_light Successfully Setup')

    log.debug('Turning Red Light on for main_light')
    main_light.red()
    sleep(2)

    log.debug('Turning Blue Light on for main_light')
    main_light.blue()
    sleep(2)

    log.debug('Turning Green Light on for main_light')
    main_light.green()
    sleep(2)

def cross_light_tests():
    cross_light = RGB(**CROSS_LIGHT_PINS)
    log.debug('cross_light Successfully Setup')

    log.debug('Turning Red Light on for cross_light')
    cross_light.red()
    sleep(2)

    log.debug('Turning Blue Light on for cross_light')
    cross_light.blue()
    sleep(2)

    log.debug('Turning Green Light on for cross_light')
    cross_light.green()
    sleep(2)

def multi_threading():
    import threading
    def test():
        for i in range(5):
            log.debug(i)
            sleep(1)

    threading.Thread(target=test)
    threading.Thread(target=test)

def display_tests():
    GPIO.setmode(GPIO.BCM)
    d = DigitDisplay(DISPLAY_PINS)
    d.display_0()

    while True:
        pass

if __name__ == '__main__':
    main()
