import RPi.GPIO as GPIO
import time

'''
BUTTONS

Buttons are in order
Yellow being the largest
Blue the 2nd digit
Black the smallest
'''
BUTTON_1 = 15 # Smallest digit 001
BUTTON_2 = 14 # 2nd digit 010
BUTTON_3 = 4 # Largest digit 100

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        while True:
            button_state = GPIO.input(BUTTON_PIN)
            if button_state == False:
                print('Button Pressed...')
                time.sleep(0.2)

    except KeyboardInterrupt:
        print('User ended the program')

    except Exception as e:
        print(e)

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()