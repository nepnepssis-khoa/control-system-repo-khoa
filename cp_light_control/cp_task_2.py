import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

while True:
    for i in range(0, 65535, 64):
        # analog output incrementing
        analog_out.value = i
    analog_out.value = 0
