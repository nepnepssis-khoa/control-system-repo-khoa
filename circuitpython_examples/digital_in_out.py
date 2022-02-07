"""CircuitPython Essentials Digital In Out example - modified by Evan Weinberg"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.LED)
# Set led pin direction
led.direction = Direction.OUTPUT

# Switch setup
switch = DigitalInOut(board.D2)
# Set direction
switch.direction = Direction.INPUT
# Set pin pull direction (for direction = input only)
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay
