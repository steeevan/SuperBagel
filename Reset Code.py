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
touchled_4 = Touchled(Ports.PORT4)
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
#       elif (abs(controller.axisC.position()) > 10  or abs(controller.axisD.position()) > 10):
#       LeftBase.spin(REVERSE,controller.axisC.position() - controller.axisD.position() * 0.7,PERCENT)
#       RightBase.spin(REVERSE,controller.axisC.position() + controller.axisD.position() * 0.7, PERCENT)
    else:
        LeftBase.stop()
        RightBase.stop()

# Functions

def motorStop(): 
    LeftBase.stop()
    RightBase.stop()
    Slapshot.stop()
    Bluetower.stop()
    Purpletower.stop()
    bucket.stop()
    

def Shooting(): 
    bucket.spin(FORWARD) and Shoot()
    WaitTime(0)
    bucket.stop() and Shoot()
    WaitTime(3)
    bucket.spin(REVERSE)
    Shoot()
    WaitTime(0.5)

def Shoot(): 
    Purpletower.spin(FORWARD)
    Slapshot.spin(FORWARD)

def StopShoot(): 
    Purpletower.stop()
    Slapshot.stop()

def WaitTime(timeinseconds): 
    wait(timeinseconds, SECONDS)

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
    WaitTime(0)
    Bluetower.spin_to_position(0, DEGREES)

def DiscDrop(): 
    Bluetower.spin_for(FORWARD, 675, DEGREES)
    WaitTime(0)
    Bluetower.spin_to_position(0, DEGREES)

def BlueTrigger(): 
    Bluetower.spin(FORWARD)
    WaitTime(2.5)
    Bluetower.spin_to_position(0, DEGREES)

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

# Bluetower Lever controls

def blue_control(): 
    controller.buttonEDown.pressed(ArmExtention)
    controller.buttonFDown.pressed(DiscDrop)
    controller.buttonEUp.pressed(BlueTrigger)

# Helper Functions (Auton.)

def Drivebase_Forward(DISTANCEINMM): 
    LeftBase.spin_for(FORWARD, DISTANCEINMM/2, DEGREES, wait=False)
    RightBase.spin_for(REVERSE, DISTANCEINMM/2, DEGREES, wait=True)

def LeftTurn(DISTANCEINMM): 
    LeftBase.spin_for(REVERSE, DISTANCEINMM, DEGREES, wait=False)
    RightBase.spin_for(REVERSE, DISTANCEINMM, DEGREES, wait=True)

def RightTurn(DISTANCEINMM): 
    LeftBase.spin_for(FORWARD, DISTANCEINMM, DEGREES, wait=False)
    RightBase.spin_for(FORWARD, DISTANCEINMM, DEGREES, wait=True)

def Drivebase_Reverse(DISTANCEINMM): 
    LeftBase.spin_for(REVERSE, DISTANCEINMM/2, DEGREES, wait=False)
    RightBase.spin_for(FORWARD, DISTANCEINMM/2, DEGREES, wait=True)

def Drivebase_Reverse2(Time): 
    LeftBase.spin(REVERSE) and RightBase.spin(FORWARD)
    WaitTime(Time)

def Drivebase_Forward2(Time): 
    LeftBase.spin(FORWARD) and RightBase.spin(REVERSE)
    WaitTime(Time)

def Purpletower_Discs(): 
    bucket.spin(FORWARD)
    WaitTime(1)
    bucket.set_position(0, DEGREES)
    bucket.spin_to_position(30, DEGREES)
    activate_purple()

def Shoot_with_DD():                                                  # DD = Disc Drop Function
    Shooting()
    Shooting()
    DiscDrop()
    Shooting()
    Shooting()
    Shooting()
    StopShoot()

def Standard_Shooting(): 
    Shooting()
    Shooting()
    Shooting()
    StopShoot()

def Yellowtower(): 
    LeftBase.spin(REVERSE) and RightBase.spin(FORWARD)
    WaitTime(2.5)
    bucket.spin(FORWARD)
    WaitTime(1)
    bucket.spin(REVERSE)
    Drivebase_Forward(200)


blue_control()

def main():
    drivebase_control()
    bucket_control()
    slapshot_control()

#controller.buttonRUp.pressed(activate_slap)
#controller.buttonRDown.pressed(deactivate_slap)

while drive_on:
    main()


#Reset

touchlednum = 0

def filler(): 
    pass

def reset(): 
    activate_slap()
    WaitTime(2.5)
    Shooting()
    Shooting()
    Shooting()
    Shooting()
    Shooting()
    
if touchled_4.released(filler): 
    touchlednum = touchlednum + 1
    if touchlednum == 1: 
        reset()
    else: 
        motorStop
