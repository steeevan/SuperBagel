#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
touchled_4 = Touchled(Ports.PORT4)
LeftBase = Motor(Ports.PORT2, False)
RightBase = Motor(Ports.PORT10, True)
Slapshot = Motor(Ports.PORT1, False)
Bluetower = Motor(Ports.PORT3, False)
Purpletower = Motor(Ports.PORT12, False)
bucket = Motor(Ports.PORT7, False)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
# 	Author:       VEX
# 	Created:
# 	Description:  VEXcode IQ Python Project
# 
# ------------------------------------------
from vex import *
#from multiprocessing import Process
# Begin project code
def set_robot_motors():
    LeftBase.set_velocity(50,PERCENT)                  # Setting driving speed to 100
    RightBase.set_velocity(50,PERCENT)
    Slapshot.set_max_torque(100,PERCENT)                #set max torque of slapshot to 100
    Slapshot.set_velocity(100,PERCENT)                  #set the velocity of Slapshot to 100
    bucket.set_velocity(100,PERCENT)                    #set velocity of bucket to 100
    Bluetower.set_velocity(100,PERCENT)                 #set blue tower speed to 100
    Purpletower.set_velocity(100,PERCENT)               #set purple tower velocity to 100
    Bluetower.set_position(0, DEGREES)
    Bluetower.set_stopping(HOLD)
    bucket.set_stopping(HOLD)

set_robot_motors()
def driveStraight_dividedistanceby2(driveStraight_distance_heading_velocity_kp__distance, driveStraight_distance_heading_velocity_kp__heading, driveStraight_distance_heading_velocity_kp__velocity, driveStraight_distance_heading_velocity_kp__kp):
    global myVariable, error, output
    LeftBase.set_position(0, DEGREES)
    RightBase.set_position(0, DEGREES)
    if driveStraight_distance_heading_velocity_kp__velocity > 0:
        while LeftBase.position(DEGREES) < driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            LeftBase.set_velocity((driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            RightBase.set_velocity((driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            LeftBase.spin(FORWARD)
            RightBase.spin(FORWARD)
            wait(20, MSEC)
    else:
        while LeftBase.position(DEGREES) > driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            LeftBase.set_velocity((driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            RightBase.set_velocity((driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            LeftBase.spin(FORWARD)
            RightBase.spin(FORWARD)
            wait(20, MSEC)
    LeftBase.stop()
    RightBase.stop()
# Setting state of variables

state_slapshot = False
purple_state = False
drive_on = True

#helper functions for autonomous
def WaitTime(timeinseconds): 
    wait(timeinseconds, SECONDS)

#def driveever():
#    LeftBase.spin(REVERSE)
#    while LeftBase.is_spinning():
#        RightBase.spin(FORWARD)
def driveMM(DrivingMM):
    LeftBase.spin_for(FORWARD,DrivingMM/2,DEGREES,wait=False)
    RightBase.spin_for(FORWARD,DrivingMM/2,DEGREES)
def leftTurn(Angle):
    RightBase.spin_for(FORWARD,Angle*2,DEGREES,wait=False)
    LeftBase.spin_for(REVERSE,Angle*2,DEGREES)    
def Shoot(): 
    Purpletower.spin(FORWARD)
    Slapshot.spin(FORWARD)
#my_list = [Process(bucket.spin(FORWARD)),Process(activate_purple()),Process(Shoot),Process(wait(2,SECONDS))]    
#def Shooting(): 
#    for t in my_list:
#        t.start()
#    for t in my_list:
#        t.join()
def Shooting():
    bucket.spin_for(FORWARD,90,DEGREES,wait=False) 
    activate_purple()
    Shoot()
    WaitTime(0)
    bucket.stop()
    Shoot()
    WaitTime(3)
    bucket.spin_for(REVERSE,90,DEGREES,wait=False)
    activate_purple()
    WaitTime(0)

def StopShoot(): 
    Purpletower.stop()
    Slapshot.stop()

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
#def DiscDrop(): 
#    Bluetower.spin_for(FORWARD, 675, DEGREES)
#    WaitTime(0)
#    Bluetower.spin_to_position(0, DEGREES)

def BlueTrigger(): 
    Bluetower.spin(FORWARD)
    WaitTime(2.5)
    Bluetower.spin_to_position(0, DEGREES)
def Bluetower_1():
    bucket.spin(FORWARD)
    wait(2,SECONDS)
    bucket.stop()
    BlueTrigger()
    #blue has been triggered yay :)
def Purple_1():
    Purpletower.spin(FORWARD)
    driveMM(30)
    wait(7,SECONDS)
    driveMM(-30)
    Purpletower.stop()
#autonomous control programs
#def distance_driver(distanceInMM):
#    while distances.object_distance(MM) > distanceInMM:
#        LeftBase.spin(FORWARD)
#        RightBase.spin(FORWARD)
#    LeftBase.stop()
#    RightBase.stop()

def touchled_control():
    touchlednum = 0
    while True:
        if touchled_4.pressing():
            touchlednum = touchlednum + 1
            wait(3,SECONDS)
            if touchlednum == 1:
                touchled_4.set_color(Color.RED)
                #distance_driver(300)
                Shooting()
                Shooting()
            elif touchlednum == 2:
                touchled_4.set_color(Color.GREEN)

            elif touchlednum == 3:
                touchlednum = 0
                touchled_4.set_color(Color.BLUE)
        else:
            pass
touchled_control()