import logging
import traceback
from RPi import GPIO


from BinaryCounter import BinaryCounter
from utils import setup_pins
from constants import BUTTON_1, BUTTON_2, BUTTON_3, LOG_CONFIG, PRINT_NUM

logging.basicConfig(**LOG_CONFIG)
log = logging.getLogger(__name__)

def main():
    GPIO.setmode(GPIO.BCM)
    
    # Setup Self Containing Binary Counter
    # Current binary value accessed with counter.value
    counter = BinaryCounter(BUTTON_1,BUTTON_2,BUTTON_3)
    setup_pins()

    log.debug('main Successfully Setup')

    try:
        while True:
            value = counter.value
            PRINT_NUM[value]()

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
