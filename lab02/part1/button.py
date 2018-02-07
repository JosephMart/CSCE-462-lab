import RPi.GPIO as GPIO
import time

BUTTON_PIN = 21
RED_PIN = 26
GREEN_PIN = 19
BLUE_PIN = 13

COLORS = [RED_PIN, GREEN_PIN, BLUE_PIN]

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    INDEX = 0

    # Setup the color pins
    for c in COLORS:
        GPIO.setup(c, GPIO.OUT)

    try:
        while True:
            button_state = GPIO.input(BUTTON_PIN)
            if button_state == False:
                INDEX = pressed(INDEX)
                print('Button Pressed...')
                time.sleep(0.2)
            else:
                depressed()

    except KeyboardInterrupt:
        print('User ended the program')

    except Exception as e:
        print(e)

    finally:
        GPIO.cleanup()

def pressed(i):
    index = i % 3
    GPIO.output(COLORS[index], True)
    return i + 1

def depressed():
    for c in COLORS:
        GPIO.output(c, False)

if __name__ == '__main__':
    main()