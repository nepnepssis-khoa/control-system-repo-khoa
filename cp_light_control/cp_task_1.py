import time
import board
from analogio import AnalogIn

input = 0
analog_in = AnalogIn(board.A1)

# input loop
while True:
    input = analog_in.value
    print(input)
    time.sleep(0.5)
