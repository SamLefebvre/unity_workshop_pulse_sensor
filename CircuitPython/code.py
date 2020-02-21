# Circuit Playground AnalogIn
# Reads the analog voltage level from a 10k potentiometer connected to GND, 3.3V, and pin A1
# and prints the results to the serial console.

# CODE FOR PULSE SENSOR !
import time
import board
import analogio
import neopixel
import random

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01, auto_write=False)

analogin = analogio.AnalogIn(board.A1)

# Source, https://www.twobitarcade.net/article/wemos-heart-rate-sensor-display-micropython/


def getVoltage(pin):  # helper
    return (pin.value * 3.3) / 65536

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

MAX_HISTORY = 250
history = []
beat = False
beats = 0

# the keyboard object!
# sleep for a bit to avoid a race condition on some systems
time.sleep(1)
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)

def keyboardOutput():
    kbd.press(Keycode.SHIFT, Keycode.B)  # press...
    kbd.release_all()  # release!

while True:
    #voltage = getVoltage(analogin)
    voltage = analogin.value

    history.append(voltage)
    history = history[-MAX_HISTORY:]
    minima, maxima = min(history), max(history)

    threshold_on = (minima + maxima * 3) // 4   # 3/4
    threshold_off = (minima + maxima) // 2      # 1/2

    pixels.fill(OFF)
    pixels.show()
    #print(voltage)
    #print((analogin.value))
    time.sleep(0.02)
    print((voltage,minima,maxima,))

    if not beat and voltage > threshold_on:
        beat = True
        keyboardOutput()
        pixels.fill(PURPLE)
        pixels.show()

    if beat and voltage < threshold_off:
        beat = False
    #print((analogin.value,))
    #print((voltage, analogin.value, random.randint(-50, 50)))