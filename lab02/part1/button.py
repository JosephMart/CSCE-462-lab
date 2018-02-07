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
    lit = False

    # Setup the color pins
    for c in COLORS:
        GPIO.setup(c, GPIO.OUT)
        GPIO.output(c, False)

    try:
        while True:
            button_state = GPIO.input(BUTTON_PIN)
            if button_state == False:
                INDEX = pressed(INDEX)
                lit = True
                print('Button Pressed...')
                time.sleep(0.2)
            elif INDEX != 0:
                lit = depressed(INDEX, lit)
                time.sleep(0.2)

    except KeyboardInterrupt:
        print('User ended the program')

    except Exception as e:
        print(e)

    finally:
        GPIO.cleanup()

def pressed(i):
    index = (i + 1) % 3
    GPIO.output(COLORS[index - 1], False)
    GPIO.output(COLORS[index], True)
    return i + 1

def depressed(i, lit):
    index = i % 3
    GPIO.output(COLORS[index ], not lit)
    return not lit

if __name__ == '__main__':
    main()