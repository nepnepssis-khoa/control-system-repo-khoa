import time
import board

import adafruit_hcrs04

sonar = adafruit_hcrs04.HCSR04(trigger.pin=board.D10, echo.pin=board.D11)

while True:
  try:
    print((sonar.distance,))
  except RuntimeError:
    print("Retrying!")
    pass
  time.sleep(0.1)
