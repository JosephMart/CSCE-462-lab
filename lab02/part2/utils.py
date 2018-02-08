import RPi.GPIO as GPIO
from time import sleep

POSITIVE = [17, 27, 22, 5, 6, 13, 19, 26]
GROUND = [16, 20, 21, 12, 25, 24, 23, 18]

FLICKER_TIME = .005

X = [22, 27, 5, 17, 19, 6, 26, 13] # Ordered of Positive
Y = [18, 23, 25, 21, 12, 20, 16, 24] # Ordered of Ground

def print_0():
    pins_off(Y[:7])
    pins_on(X[2])
    pins_on(X[5])
    flicker()

    pins_on(X[3:5])
    pins_off([Y[0], Y[6]])
    flicker()

def print_1():
    pins_off(Y[:7])
    pins_on(X[5])
    flicker()

def print_2():
    pins_on(X[2:6])
    pins_off([Y[0], Y[3], Y[6]])
    flicker()

    pins_on(X[5])
    pins_off(Y[4:6])
    flicker()

    pins_on(X[2])
    pins_off(Y[0:4])
    flicker()

def print_3():
    pins_off(Y[:7])
    pins_on(X[5])
    flicker()

    pins_on(X[2:5])
    pins_off([Y[0], Y[3], Y[6]])
    flicker()

def print_4():
    pins_on(X[2:6])
    pins_off(Y[3])
    flicker()

    pins_on(X[2])
    pins_off(Y[4:7])
    flicker()

    pins_on(X[5])
    pins_off(Y[:7])
    flicker()

def print_5():
    pins_on(X[2:6])
    pins_off([Y[0], Y[3], Y[6]])
    flicker()

    pins_on(X[2])
    pins_off(Y[4:6])
    flicker()

    pins_on(X[5])
    pins_off(Y[0:4])
    flicker()

def print_6():
    pins_off(Y[:7])
    pins_on(X[2])
    flicker()

    pins_off(Y[:4])
    pins_on(X[2])
    pins_on(X[5])
    flicker()

    pins_on(X[2:6])
    pins_off([Y[0], Y[3], Y[6]])
    flicker()


def print_7():
    pins_off(Y[:7])
    pins_on(X[5])
    flicker()

    pins_on(X[2:6])
    pins_off(Y[6])
    flicker()

def print_8():
    pins_off(Y[:7])
    pins_on(X[2])
    pins_on(X[5])
    flicker()

    pins_on(X[3:5])
    pins_off([Y[0], Y[3], Y[6]])
    flicker()


def setup_pins():
    GPIO.setup(GROUND + POSITIVE, GPIO.OUT)
    reset_pins()

def reset_pins():
    pins_on(Y)
    pins_off(X)

def flicker():
    sleep(FLICKER_TIME)
    reset_pins()

def pins_on(pins):
    GPIO.output(pins, True)

def pins_off(pins):
    GPIO.output(pins, False)