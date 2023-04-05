def driveStraight_distance_heading_velocity_kp(driveStraight_distance_heading_velocity_kp__distance, driveStraight_distance_heading_velocity_kp__heading, driveStraight_distance_heading_velocity_kp__velocity, driveStraight_distance_heading_velocity_kp__kp):
    global myVariable, error, output
    LeftMotor.set_position(0, DEGREES)
    RightMotor.set_position(0, DEGREES)
    if driveStraight_distance_heading_velocity_kp__velocity > 0:
        while LeftMotor.position(DEGREES) < driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            LeftMotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            RightMotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            LeftMotor.spin(FORWARD)
            RightMotor.spin(FORWARD)
            wait(20, MSEC)
    else:
        while LeftMotor.position(DEGREES) > driveStraight_distance_heading_velocity_kp__distance:
            error = driveStraight_distance_heading_velocity_kp__heading - brain_inertial.rotation()
            output = error * driveStraight_distance_heading_velocity_kp__kp
            LeftMotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity - output), PERCENT)
            RightMotor.set_velocity((driveStraight_distance_heading_velocity_kp__velocity + output), PERCENT)
            LeftMotor.spin(FORWARD)
            RightMotor.spin(FORWARD)
            wait(20, MSEC)
    LeftMotor.stop()
    RightMotor.stop()
