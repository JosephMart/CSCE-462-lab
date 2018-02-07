from RPi import GPIO
import traceback
from BinaryCounter import BinaryCounter
from constants import BUTTON_1, BUTTON_2, BUTTON_3


def main():
    GPIO.setmode(GPIO.BCM)
    
    # Setup Self Containing Binary Counter
    # Current binary value accessed with counter.value
    counter = BinaryCounter(BUTTON_1,BUTTON_2,BUTTON_3)

    try:
        while True:
            value = counter.value

    except KeyboardInterrupt:
        print('User ended the program')

    except Exception as e:
        var = traceback.format_exc()
        print(e)
        print(str(var))

    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()