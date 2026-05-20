######################## Pyricks library ########################
from pybricks.parameters import Color, Direction, Stop, Icon, Button
from pybricks.tools import wait, StopWatch
from ACL_FLL_v04_test import *

################## Shared and local constants ##################

# Adapter configuration: (LeftPower, RightPower, LeftLimit, RightLimit)
ROUTE_ADAPTER_POWER = (-40, 40, 30, 30)

# Route-Specific PID Gains
STR_KP_CUSTOM = 1.5
STR_KD_CUSTOM = 1

GYRO_KP_CUSTOM = 0.7
GYRO_KD_CUSTOM = 0.2

LF_KP_CUSTOM = 0.4
LF_KD_CUSTOM = 0.1

######################## Route program ########################

# --- Starting position ---
# Blue base - Robot right wheel align 1st line from right
# Mission - Mountain rock

def Route5(laura: Laura):

    print("\n--- Starting Route 6 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    # Step 1 - Go to brush area
    laura.wall_square(power=35,duration=200)
    laura.gyro_acc(-90,600,decel_dist=130,stop=False)
    laura.gyro_lock_turn(port= RIGHT_DRIVE , angle= 45 , stop= False)
    laura.gyro_lock_turn(port= LEFT_DRIVE ,angle= 0 , stop= False)
    laura.gyro_acc(power= -70 , distance= 55 , stop= True)
    # laura.gyro_time(power= -45 , duration= 1000)
    # laura.gyro_acc(power= 50 , distance= 110,decel_dist=130,stop=True)
    laura.adapter_motor_seconds(RIGHT_ADAPTER,-800,600,wait_complete=False)
    laura.encoder_time(left_power= -60 , right_power= 60 , duration= 600)
    laura.gyro_sensor(power= 45 , port= LEFT_COLOUR , threshold= 70 , compare= False , angle= -90 )
    laura.adapter_motor_seconds(LEFT_ADAPTER,400,600,wait_complete=False)
    wait(200)
    laura.gyro_time(power= 45 , duration= 600 , angle= -90)
    laura.adapter_motor_seconds(LEFT_ADAPTER,-300,600,wait_complete=False)
    laura.adapter_motor_seconds(RIGHT_ADAPTER,300,800,wait_complete=True)
    wait(200)
    laura.gyro_degree(power= -50 , degree= 260 , angle= -93 , stop= False)
    laura.gyro_point_turn(angle= 15 , stop= False)
    laura.gyro_acc(power= 80 , distance= 450 , angle= 15 , stop= False)
    laura.gyro_acc(power= 80 , distance= 240 )
    # laura.gyro_point_turn(angle= -180 , stop= False)
    # laura.gyro_acc(power= -80 , distance= 300 , angle= -180)
    
    # laura.move_curve_angle(200,90,650,900,Stop.BRAKE,True)
    
    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 6 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.RIGHT in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route5(test)