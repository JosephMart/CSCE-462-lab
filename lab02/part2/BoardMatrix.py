import RPi.GPIO as GPIO
from time import sleep
from constants import POSITIVE, GROUND

class BoardMatrix:
    def __init__(self):
        self.__pin