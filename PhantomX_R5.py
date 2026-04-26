######################## Pyricks library ########################
from pybricks.parameters import Color, Direction, Stop, Icon, Button
from pybricks.tools import wait, StopWatch
from ACL_FLL_v04_test import *

################## Shared and local constants ##################

# Adapter configuration: (LeftPower, RightPower, LeftLimit, RightLimit)
ROUTE_ADAPTER_POWER = (-35, -35, 30, 30)

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

    print("\n--- Starting Route 5 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    laura.wall_square(power=35)
    laura.gyro_acc(power= -80 , distance= 550)
    laura.gyro_point_turn(46)
    laura.gyro_acc(power= -50 , distance= 115 , angle= 45)
    laura.gyro_point_turn(angle= -46)
    laura.gyro_acc(power= -50 , distance= 150 , angle= -45 , stop= False)
    laura.gyro_time(power= -35 , duration= 1200 , angle= -45)
    laura.adapter_motor_seconds( port= LEFT_ADAPTER , speed= 1000 , duration= 1000)
    laura.gyro_acc( power= 50 , distance= 150 , angle= -45)
    laura.gyro_lock_turn( port= LEFT_DRIVE , angle= 0)
    laura.gyro_acc( power= 60 , distance= 40)
    laura.adapter_motor_seconds( port=RIGHT_ADAPTER , speed=1000 , duration= 1200, wait_complete= False)
    laura.gyro_point_turn(angle= 90)
    laura.gyro_time(power= 40 , duration= 1200 , angle= 88)
    laura.adapter_motor_seconds( port=RIGHT_ADAPTER , speed= -1000 , duration= 1200 )
    laura.adapter_motor_seconds( port=RIGHT_ADAPTER , speed= 1000 , duration= 1200 )
    laura.gyro_acc( power= -60 , distance= 100 , angle= 90)
    laura.gyro_point_turn(angle= 200)
    laura.gyro_acc( power= -70 , distance= 600 , angle= 200)
    



    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 5 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.RIGHT in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route5(test)
