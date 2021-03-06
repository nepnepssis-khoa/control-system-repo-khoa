"""CircuitPython Analog Out example"""
import board
from analogio import AnalogOut

# set output to pin A0, only pin without true analog output
analog_out = AnalogOut(board.A0)

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    for i in range(0, 65535, 64):
        # analog output incrementing
        analog_out.value = i
