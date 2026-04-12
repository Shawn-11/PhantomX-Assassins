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

def Route4(laura: Laura):

    print("\n--- Starting Route 4 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    laura.wall_square()
    laura.gyro_acc(80, 790, 0, 45, 80, 250, False)
    laura.line_follow_degree(1, 40, LEFT_COLOUR, 280, False)
    laura.gyro_acc(70, 110)
    laura.gyro_lock_turn(RIGHT_DRIVE, 90)
    laura.adapter_motor_seconds(LEFT_ADAPTER, -800, 1200, Stop.COAST, False)
    laura.line_follow_degree(-1, 40, RIGHT_COLOUR, 130, False)
    laura.gyro_lock_turn(RIGHT_DRIVE, 66)
    laura.gyro_acc(60, 100, 66)
    laura.adapter_motor_seconds(LEFT_ADAPTER, 450, 1400, Stop.BRAKE, False)
    wait(300)
    laura.gyro_lock_turn(RIGHT_DRIVE, 90)
    



    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 4 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.RIGHT in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route4(test)
