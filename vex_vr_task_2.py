from math import *
from random import randint

def generateRandomPoint():
    xCoordinate = randint(-4,8)*100
    yCoordinate = randint(-4,8)*100
    return [xCoordinate,yCoordinate]
def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXpos = location.position(X,MM)
        error = setpoint - currentXpos
        velocity = 0.5*error

        drivetrain.set_drive_velocity(velocity,PERCENT)

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
        error = setpoint - currentYpos
        velocity = 0.5*error

        drivetrain.set_drive_velocity(velocity,PERCENT)

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


def driveUsingDistanceSensor(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXpos = distance.get_distance(MM)
        error = currentXpos - setpoint
        velocity = 0.5*error

        drivetrain.set_drive_velocity(velocity,PERCENT)

        # Your code goes here!
        if(currentXpos > setpoint):
            drivetrain.drive(FORWARD)
        elif(currentXpos < setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    # You should not change much in the code below. This code chooses a random point, puts the pen down,
    # and then calls the above functions to move to the point, turn to face the right wall, and then move the specified distance away.
    target = generateRandomPoint()
    brain.print("target location is x = ( " + str(target[0]) + " , " + str(target[1]) + " )" )
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(target[0],4)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(target[1],4)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveUsingDistanceSensor(200,5)
# VR threads — Do not delete
vr_thread(main())
