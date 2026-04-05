######################## Pyricks library ########################
from pybricks.parameters import Color, Direction, Stop, Icon, Button
from pybricks.tools import wait, StopWatch
from ACL_FLL_v04_test import *

################## Shared and local constants ##################

# Adapter configuration: (LeftPower, RightPower, LeftLimit, RightLimit)
ROUTE_ADAPTER_POWER = (-40, 0, 30, 30)

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

def Route3(laura):

    print("\n--- Starting Route 3 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    # Step 1 - Go to mountain
    laura.wall_square()
    laura.gyro_acc(power= 80 , distance= 380 , decel_dist= 0, stop=False)
    laura.gyro_time(power= 40 ,duration= 700)
    

    # Step 2 - solve mission
    for i in range(4):
        laura.adapter_motor_seconds(LEFT_ADAPTER, speed= 750 , duration= 600 , stop_method=Stop.COAST)
        laura.adapter_motor_seconds(LEFT_ADAPTER, speed= -700 , duration= 500 , stop_method=Stop.COAST)
        laura.encoder_time(left_power= 30 , right_power= 20 , duration= 200,stop=False)

    # Step 3 - Back to base
    laura.gyro_acc(power= -80 , distance= 370,stop=False)


    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 3 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.BLUETOOTH in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route3(test)