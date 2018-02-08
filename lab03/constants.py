import logging

# Debounce time for buttone press
BOUNCE_TIME = 500
LOG_FILENAME = 'pins.log'
LOG_FORMAT = '%(levelname)s | %(asctime)-15s | %(message)s'
LOG_CONFIG = {
    'format': LOG_FORMAT,
    'level': logging.DEBUG,
    'filename': LOG_FILENAME
}

MAIN_LIGHT_PINS = {
    'red_pin': 16,
    'green_pin': 20,
    'blue_pin': 21
}

CROSS_LIGHT_PINS = {
    'red_pin': 13,
    'green_pin': 19,
    'blue_pin': 26
}

BOUNCE_TIME = 30000
BUTTON_PIN = 12

DISPLAY_PINS = {
    'a': 18,
    'b': 23,
    'c': 24,
    'd': 27,
    'e': 17,
    'f': 22,
    'g': 5
}
