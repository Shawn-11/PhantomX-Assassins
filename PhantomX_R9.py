######################## Pyricks library ########################
from pybricks.parameters import Color, Direction, Stop, Icon, Button
from pybricks.tools import wait, StopWatch
from ACL_FLL_v04_test import *

################## Shared and local constants ##################

# Adapter configuration: (LeftPower, RightPower, LeftLimit, RightLimit)
ROUTE_ADAPTER_POWER = (40, -40, 30, 30)

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

def Route9(laura: Laura):

    print("\n--- Starting Route 9 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    laura.wall_square()
    laura.adapter_motor_seconds(port= LEFT_ADAPTER , speed= 1000 , duration= 1000 , wait_complete= False)
    laura.gyro_acc(power= 80 , distance= 770 , stop= False)
    laura.line_follow_degree(direction= -1 , power= 50 ,port= RIGHT_COLOUR ,degree= 80 , stop= False )
    laura.line_follow_detect_reflected(direction= -1 , power= 50 ,port= RIGHT_COLOUR , detect_port= LEFT_COLOUR , threshold= 30)
    laura.encoder_degree(left_power= -70 , right_power= 70 , degree= 140 , stop= False)   
    laura.gyro_acc(power= 80 , distance= 480 , angle= -64)
    laura.gyro_lock_turn(LEFT_DRIVE, 0)
    laura.gyro_lock_turn(RIGHT_DRIVE, -50)
    laura.gyro_lock_turn(LEFT_DRIVE, -90)
    laura.gyro_degree(60, 230, -90, False)
    laura.gyro_degree(60, 50, -90, True)
    laura.adapter_motor_seconds(port= LEFT_ADAPTER , speed= -1000 , duration= 1200 , wait_complete=False)
    laura.adapter_motor_seconds(RIGHT_ADAPTER, 1000, 3000, wait_complete=True)
    laura.gyro_lock_turn(RIGHT_DRIVE, -56, False)
    laura.gyro_acc(-80, 700, -56, stop=False)
    laura.gyro_point_turn(-100)
    laura.adapter_motor_seconds(RIGHT_ADAPTER, -1000, 2200)
    laura.gyro_point_turn(0, True, 90, 0)


    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 9 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.RIGHT in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route9(test)
