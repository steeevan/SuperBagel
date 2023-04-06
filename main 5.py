#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
LeftBase = Motor(Ports.PORT2, False)
RightBase = Motor(Ports.PORT10, False)
Slapshot = Motor(Ports.PORT1, False)
Bluetower = Motor(Ports.PORT3, False)
Purpletower = Motor(Ports.PORT12, False)
bucket = Motor(Ports.PORT7, False)
controller = Controller()
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
# 	Author:       VEX
# 	Created:
# 	Description:  VEXcode IQ Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
def set_robot_motors():
    LeftBase.set_velocity(100,PERCENT)                  # Setting driving speed to 100
    RightBase.set_velocity(100,PERCENT)
    Slapshot.set_max_torque(100,PERCENT)                #set max torque of slapshot to 100
    Slapshot.set_velocity(100,PERCENT)                  #set the velocity of Slapshot to 100
    bucket.set_velocity(100,PERCENT)                    #set velocity of bucket to 100
    Bluetower.set_velocity(100,PERCENT)                 #set blue tower speed to 100
    Purpletower.set_velocity(100,PERCENT)               #set purple tower velocity to 100
    Bluetower.set_position(0, DEGREES)
    Bluetower.set_stopping(HOLD)


set_robot_motors()

# Setting state of variables

state_slapshot = False
purple_state = False
drive_on = True

# Setting drivebase control

def drivebase_control():
    if (abs(controller.axisA.position()) > 10  or abs(controller.axisC.position()) > 10):
        LeftBase.spin(FORWARD,controller.axisA.position() + controller.axisC.position() * 0.7,PERCENT)
        RightBase.spin(REVERSE,controller.axisA.position() - controller.axisC.position() * 0.7, PERCENT)
#    elif (abs(controller.axisC.position()) > 10  or abs(controller.axisD.position()) > 10):
#        LeftBase.spin(REVERSE,controller.axisC.position() - controller.axisD.position() * 0.7,PERCENT)
#        RightBase.spin(REVERSE,controller.axisC.position() + controller.axisD.position() * 0.7, PERCENT)
    else:
        LeftBase.stop()
        RightBase.stop()

# Functions

def activate_slap():
    Slapshot.spin(FORWARD)
    
def deactivate_slap():
    Slapshot.stop()

def activate_purple():
    Purpletower.spin(REVERSE)

def deactivate_purple():
    Purpletower.stop()

def BlueTrigger(): 
    if controller.buttonEUp.pressing():
        brain.screen.print(Bluetower.position(DEGREES))
        brain.screen.next_row()
        if Bluetower.position(DEGREES) < 100:
            Bluetower.spin_for(FORWARD,10,DEGREES,wait=False)
        if Bluetower.position(DEGREES) > 100:
            Bluetower.stop()
            Bluetower.spin_to_position(0,DEGREES)
    elif controller.buttonEDown.pressing():
        if Bluetower.position(DEGREES) < 360:
            Bluetower.spin_for(FORWARD,10,DEGREES,wait=False)
        if Bluetower.position(DEGREES) > 360:
            Bluetower.stop()
            Bluetower.spin_to_position(0,DEGREES)
    elif controller.buttonFDown.pressing():
        if Bluetower.position(DEGREES) < 620:
            Bluetower.spin_for(FORWARD,10,DEGREES,wait=False)
        if Bluetower.position(DEGREES) > 620:
            Bluetower.stop()
            Bluetower.spin_to_position(0,DEGREES)
    else:
        Bluetower.stop()
# Bucket & Purpletower functions

def bucket_control():
    if controller.buttonLUp.pressing():
        bucket.spin(FORWARD)
        activate_purple()

    elif controller.buttonLDown.pressing():
        bucket.spin(REVERSE)
        deactivate_purple()
    elif controller.buttonFUp.pressing():
        activate_purple()
    else:
        bucket.stop()
        deactivate_purple()
        
# Slapshot controls

def slapshot_control():
    if controller.buttonRUp.pressing():
        Slapshot.spin(FORWARD)
    if controller.buttonRDown.pressing():
        Slapshot.stop()
    



def main():
    drivebase_control()
    bucket_control()
    slapshot_control()
    BlueTrigger()

#controller.buttonRUp.pressed(activate_slap)
#controller.buttonRDown.pressed(deactivate_slap)
    
while drive_on:
    main()