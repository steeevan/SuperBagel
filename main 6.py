#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
LeftBase = Motor(Ports.PORT2, False)
RightBase = Motor(Ports.PORT10, True)
Slapshot = Motor(Ports.PORT1, False)
Bluetower = Motor(Ports.PORT3, False)
Purpletower = Motor(Ports.PORT12, False)
bucket = Motor(Ports.PORT7, False)
controller = Controller()
touchled_4 = Touchled(Ports.PORT4)
distances = Distance(Ports.PORT6)
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


set_robot_motors()

# Setting state of variables

state_slapshot = False
purple_state = False
drive_on = True

#helper functinos for autonomous
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
def Shooting(): 
    bucket.spin(FORWARD) and Shoot()
    WaitTime(0)
    bucket.stop() and Shoot()
    WaitTime(3)
    bucket.spin(REVERSE)
    activate_purple()
    WaitTime(0)

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
#def DiscDrop(): 
#    Bluetower.spin_for(FORWARD, 675, DEGREES)
#    WaitTime(0)
#    Bluetower.spin_to_position(0, DEGREES)

def BlueTrigger(): 
    Bluetower.spin(FORWARD)
    WaitTime(2.5)
    Bluetower.spin_to_position(0, DEGREES)
def Leftprogram():
    driveMM(560)
    leftTurn(-45)
    wait(5,SECONDS)
    driveMM(1000)
    wait(5,SECONDS)
    leftTurn(45)
    wait(5,SECONDS)
    LeftBase.stop()
    RightBase.stop()
    #driveever()
    wait(10,SECONDS)
    driveMM(-200)
    LeftBase.stop()
    RightBase.stop()
    BlueTrigger()
    driveMM(200)
    leftTurn(20)
    driveMM(100)
    leftTurn(-20)
    Shooting()
    Shooting()
#autonomous control programs
def distance_driver(distanceInMM):
    while distances.object_distance(MM) > distanceInMM:
        LeftBase.spin(FORWARD)
        RightBase.spin(FORWARD)
    LeftBase.stop()
    RightBase.stop()

def touchled_control():
    touchlednum = 0
    while True:
        if touchled_4.pressing():
            touchlednum = touchlednum + 1
            wait(3,SECONDS)
            if touchlednum == 1:
                touchled_4.set_color(Color.RED)
                #distance_driver(300)
                Leftprogram()
            elif touchlednum == 2:
                touchled_4.set_color(Color.GREEN)
            
            elif touchlednum == 3:
                touchlednum = 0
                touchled_4.set_color(Color.BLUE)
        else:
            pass
touchled_control()