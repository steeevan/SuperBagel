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
gyro_5 = Gyro(Ports.PORT5)
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
    Bluetower.set_position(0, DEGREES)                  #set position of Blue
    Bluetower.set_stopping(HOLD)                        #set stopping of Blue
    bucket.set_stopping(HOLD)                           #set stopping of bucket

#set_robot_motors()
def driveStraight_dividedistanceby2(driveStraight_distance_heading_velocity_kp__distance, driveStraight_distance_heading_velocity_kp__heading, driveStraight_distance_heading_velocity_kp__velocity, driveStraight_distance_heading_velocity_kp__kp):
    global myVariable, error, output
    #drives very Straight and works very well
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
def driveReverse_dividedistanceby2(driveStraight_distance_heading_velocity_kp__distance, driveStraight_distance_heading_velocity_kp__heading, driveStraight_distance_heading_velocity_kp__velocity, driveStraight_distance_heading_velocity_kp__kp):
    global myVariable, error, output
    #drives very Straight and works very well
    LeftBase.set_position(0, DEGREES)
    RightBase.set_position(0, DEGREES)
    if driveStraight_distance_heading_velocity_kp__velocity > 0:
        while LeftBase.position(DEGREES) < driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            LeftBase.set_velocity(-(driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            RightBase.set_velocity(-(driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            LeftBase.spin(FORWARD)
            RightBase.spin(FORWARD)
            wait(20, MSEC)
    else:
        while LeftBase.position(DEGREES) > driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            LeftBase.set_velocity(-(driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            RightBase.set_velocity(-(driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            LeftBase.spin(FORWARD)
            RightBase.spin(FORWARD)
            wait(20, MSEC)
    LeftBase.stop()
    RightBase.stop()

def turn_heading_velocity_momentum(turn_heading_velocity_momentum__heading, turn_heading_velocity_momentum__velocity, turn_heading_velocity_momentum__momentum):
    if turn_heading_velocity_momentum__heading > brain_inertial.rotation():
        # left
        while turn_heading_velocity_momentum__heading - turn_heading_velocity_momentum__momentum > gyro_5.rotation():
            LeftBase.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            RightBase.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            LeftBase.spin(REVERSE)
            RightBase.spin(REVERSE)
            wait(20, MSEC)
    else:
        # right
        while turn_heading_velocity_momentum__heading + turn_heading_velocity_momentum__momentum < gyro_5.rotation():
            LeftBase.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            RightBase.set_velocity(turn_heading_velocity_momentum__velocity, PERCENT)
            LeftBase.spin(REVERSE)
            RightBase.spin(REVERSE)
            wait(20, MSEC)
    LeftBase.stop()
    RightBase.stop()



# Setting state of variables

state_slapshot = False
purple_state = False
drive_on = True

#helper functions for autonomous
def WaitTime(timeinseconds): 
    #wait time very precise
    wait(timeinseconds, SECONDS)

#def driveever():
#    LeftBase.spin(REVERSE)
#    while LeftBase.is_spinning():
#        RightBase.spin(FORWARD)
def driveMM(DrivingMM):
    #drives but not as precise
    LeftBase.spin_for(FORWARD,DrivingMM/2,DEGREES,wait=False)
    RightBase.spin_for(FORWARD,DrivingMM/2,DEGREES)
def leftTurn(Angle):
    #for turning
    RightBase.spin_for(FORWARD,Angle*2,DEGREES,wait=False)
    LeftBase.spin_for(REVERSE,Angle*2,DEGREES)
def Shooting():
    #shoots disks
    Purpletower.spin(REVERSE)
    Slapshot.spin(FORWARD)
    bucket.spin_for(FORWARD,170,DEGREES,wait=False)
    wait(1,SECONDS)
    bucket.stop()
    driveMM(100)
    wait(1,MSEC)
    driveMM(-100)
    WaitTime(1)
    bucket.spin_for(REVERSE,170,DEGREES,wait=False)
    wait(1,SECONDS)
def StopShoot(): 
    #stops shooting
    Purpletower.stop()
    Slapshot.stop()
def activate_arm():
    #activates bluetower
    Bluetower.spin(FORWARD)
    wait(1,SECONDS)
    Bluetower.stop()
def activate_slap():
    #activates the slapshot
    Slapshot.spin(FORWARD)
def deactivate_slap():
    #deactivats the slashot 
    Slapshot.stop()
def activate_purple():
    #purple start
    Purpletower.spin(REVERSE)
def deactivate_purple():
    #purple stop
    Purpletower.stop()

def ArmExtention(): 
    #arm extention to get 4 point zone! :)
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
    #purple start and go forward to activate
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
def yellow_get_ready():
    #put the bucket for yellow down
    bucket.spin(REVERSE)
    wait(1,SECONDS)
    bucket.stop()
def yellow_activate():
    #yellow already in position
    bucket.spin(FORWARD)
    wait(10,MSEC)
    bucket.stop()
    driveStraight_dividedistanceby2(25,0,60,2)
    wait(1,SECONDS)
    driveReverse_dividedistanceby2(25,0,60,2)
    bucket.spin(REVERSE)
    wait(10,MSEC)
    bucket.stop()
def actual_autostart():
    driveStraight_dividedistanceby2(-150,0,60,2)
    yellow_activate()
    driveStraight_dividedistanceby2(100,0,60,2)
    leftTurn(150)
    driveStraight_dividedistanceby2(250,210,60,2)
    leftTurn(30)
    driveStraight_dividedistanceby2(-100,-180,60,2)
    BlueTrigger()
    driveStraight_dividedistanceby2(150,-180,60,2)
def touchled_control():
    touchlednum = 0
    while True:
        brain_inertial.set_heading(0,DEGREES)
        if touchled_4.pressing():
            touchlednum = touchlednum + 1
            wait(0.25,SECONDS)
            if touchlednum == 1:
                touchled_4.set_color(Color.RED)
                #actual_autostart()
                #driveStraight_dividedistanceby2(150,0,60,2)
                #turn_heading_velocity_momentum(90,10,2)
                #driveReverse_dividedistanceby2(150,0,60,4)
                yellow_activate()
            elif touchlednum == 2:
                touchled_4.set_color(Color.GREEN)

            elif touchlednum == 3:
                touchlednum = 0
                touchled_4.set_color(Color.BLUE)
        else:
            pass
set_robot_motors()
brain.screen.print("Motors have been set.")
brain_inertial.calibrate()
brain.screen.print("Brain_inertial has been calibrated. ")
touchled_control()
