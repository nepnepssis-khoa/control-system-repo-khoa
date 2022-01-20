from AnalogSensorSim import WaterFlowValve

myWaterValve = WaterFlowValve()
currentValue = 0.0


#Your task is to send the valve a correct signal to get the flow rate to be 4.5 L/s.

currentTime = 0.0
currentSignal = 150
setpoint = 4.5
error = 0
sum_error = 0
last_error = 0

while(currentTime < 10.0):
  valveFlowSensorValue = myWaterValve.getFlowRate()
  
  k = 10
  kI = 1
  kD = 10

  error = setpoint - valveFlowSensorValue
  sum_error += error
  change_error = error - last_error

  currentSignal += k*error + kI*sum_error +kD*change_error
  last_error = error

  myWaterValve.setSignal(currentSignal)




  print(currentTime,",",valveFlowSensorValue)
  currentTime += 0.1

