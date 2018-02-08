import logging
from utils import *
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

# Debounce time for buttone press
BOUNCE_TIME = 500
LOG_FILENAME = 'pins.log'
LOG_FORMAT = '%(levelname)s | %(asctime)-15s | %(message)s'
LOG_CONFIG = {
    'format': LOG_FORMAT,
    'level': logging.DEBUG,
    'filename': LOG_FILENAME
}

# Ground and High Pins
POSITIVE = [17, 27, 22, 5, 6, 13, 19, 26]
GROUND = [16, 20, 21, 12, 25, 24, 23, 18]

PRINT_NUM = {
    bin(0): print_0,
    bin(1): print_1,
    bin(2): print_2,
    bin(3): print_3,
    bin(4): print_4,
    bin(5): print_5,
    bin(6): print_6,
    bin(7): print_7,
    bin(8): print_8
}