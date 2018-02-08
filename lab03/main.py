import logging
import traceback
from RPi import GPIO
from time import sleep
from multiprocessing import Process

from constants import LOG_CONFIG, MAIN_LIGHT_PINS, CROSS_LIGHT_PINS, BOUNCE_TIME, BUTTON_PIN
from rgb import RGB
from button import Button
from digit_display import DigitDisplay
from fsm import FSM

logging.basicConfig(**LOG_CONFIG)
log = logging.getLogger(__name__)

def main():
    try:
        state_machine = FSM()
        state_machine.start()

    except KeyboardInterrupt:
        log.debug('User ended the program')

    except Exception as e:
        var = traceback.format_exc()
        log.debug(e)
        log.debug(str(var))


    finally:
        GPIO.cleanup()
        log.debug('Main Cleaned Up')

if __name__ == '__main__':
    main()
