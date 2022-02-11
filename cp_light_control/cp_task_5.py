import board
from analogio import AnalogOut

analog_in = AnalogIn(board.A1)

analog_out = AnalogOut(board.A0)

analog_out.value = 60000

while True:
  print(analog_in.value)
  time.sleep(0.1)
