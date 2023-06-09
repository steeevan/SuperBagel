#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
Slapshot = Motor(Ports.PORT1, False)
Bluetower = Motor(Ports.PORT3, False)
Purpletower = Motor(Ports.PORT12, False)
bucket = Motor(Ports.PORT7, False)
controller = Controller()
LeftBase = Motor(Ports.PORT2, False)
RightBase = Motor(Ports.PORT10, False)
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
    LeftBase.set_velocity(100,PERCENT)          # Setting driving speed to 100
    RightBase.set_velocity(100,PERCENT)
    Slapshot.set_max_torque(100,PERCENT)                #set max torque of slapshot to 100
    Slapshot.set_velocity(100,PERCENT)                  #set the velocity of Slapshot to 100
    bucket.set_velocity(100,PERCENT)                    #set velocity of bucket to 100
    Bluetower.set_velocity(100,PERCENT)                 #set blue tower speed to 100
    Purpletower.set_velocity(100,PERCENT)               #set purple tower velocity to 100
    Bluetower.set_position(0, DEGREES)



set_robot_motors()
state_slapshot = False
purple_state = False
drive_on = True

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


def activate_slap():
    Slapshot.spin(FORWARD)

def deactivate_slap():
    Slapshot.stop()

def activate_purple():
    Purpletower.spin(REVERSE)

def deactivate_purple():
    Purpletower.stop()

def ArmExtention(): 
    Bluetower.spin_for(FORWARD, 480, DEGREES)
    wait(0, SECONDS)
    Bluetower.spin_to_position(0, DEGREES)

def DiscDrop(): 
    Bluetower.spin_for(FORWARD, 675, DEGREES)
    wait(0, SECONDS)
    Bluetower.spin_to_position(0, DEGREES)

def BlueTrigger(): 
    Bluetower.spin_for(FORWARD, 107, DEGREES,wait=True)
    wait(1, SECONDS)
    Bluetower.spin_to_position(0, DEGREES)

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
        

def slapshot_control():
    if controller.buttonRUp.pressing():
        Slapshot.spin(FORWARD)
    if controller.buttonRDown.pressing():
        Slapshot.stop()
    
    
def blue_control(): 
    controller.buttonEDown.pressed(ArmExtention)
    controller.buttonFDown.pressed(DiscDrop)
    controller.buttonEUp.pressed(BlueTrigger)

blue_control()


def main():
    drivebase_control()
    bucket_control()
    slapshot_control()

#controller.buttonRUp.pressed(activate_slap)
#controller.buttonRDown.pressed(deactivate_slap)
    
while drive_on:
    main()
