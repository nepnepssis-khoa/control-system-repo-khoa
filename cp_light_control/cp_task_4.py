import board
from analogio import AnalogOut

analog_in = AnalogIn(board.A1)

analog_out = AnalogOut(board.A0)

light = 0

while True:
  light = analog_in.value
  analog_out.value = light
  time.sleep(0.1)
