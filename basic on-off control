from math import *
from random import randint

def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXpos = location.position(X,MM)
        # Your code goes here!
        if(currentXpos < setpoint):
            drivetrain.drive(FORWARD)
        elif(currentXpos > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentYpos = location.position(Y,MM)
        # Your code goes here!
        if(currentYpos < setpoint):
            drivetrain.drive(FORWARD)
        elif(currentYpos > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXpos = location.position(X,MM)
        currentYpos = location.position(Y,MM)
        # Your code goes here!
        if(currentXpos < setpoint):
            if(currentYpos < setpoint):
                drivetrain.drive(FORWARD)
        elif(currentXpos > setpoint):
            if(currentYpos > setpoint):
                drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()


        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,5)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,5)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(400,5)
# VR threads — Do not delete
vr_thread(main())
