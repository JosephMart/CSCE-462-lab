import logging
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