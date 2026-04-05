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

def Route2(laura):

    print("\n--- Starting Route 2 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    # Step 1 - Go to forge
    laura.wall_square()
    laura.gyro_lock_turn(RIGHT_DRIVE,angle= -22 ,stop=False)
    laura.gyro_acc(power= 90 , distance= 720 , angle= -22 , decel_dist=120)
    laura.gyro_point_turn(angle= 46)   # < take noted this angle
    laura.adapter_motor_seconds(RIGHT_ADAPTER, speed= 200 , duration= 1200,stop_method=Stop.BRAKE,wait_complete=False)
    wait(400)
    laura.gyro_degree(power= 60 , degree= 155, angle= 46 , stop= False)
    laura.gyro_time(power= 40 ,duration= 1000 , angle= 46)

    # # Step 2 - Solve mission

    laura.adapter_motor_seconds(LEFT_ADAPTER, speed= -1000 , duration= 1000 , stop_method=Stop.HOLD)
    laura.adapter_motor_seconds(LEFT_ADAPTER,speed= 1000 , duration= 450 , wait_complete= False)
    # laura.adapter_motor_seconds(RIGHT_ADAPTER,speed= -100 , duration= 300)
    laura.adapter_motor_seconds(RIGHT_ADAPTER, speed= -200 , duration= 1200)
    wait(150)
    laura.adapter_motor_seconds(LEFT_ADAPTER,speed= 1000 , duration= 800 , wait_complete= False)
    # # Step 3 - Back to base
    laura.gyro_acc(power= -70 , distance= 120 ,angle= 46 , decel_dist= 0 , stop= False)
    laura.adapter_motor_seconds(LEFT_ADAPTER,speed= 1000 , duration= 1250 , wait_complete= False)
    laura.gyro_point_turn(angle= -20 , stop= False)
    laura.gyro_acc(power= -90 , distance= 670 , angle= -20,stop=False)
    laura.gyro_lock_turn(RIGHT_DRIVE,angle= 0 ,stop=False)


    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 2 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.BLUETOOTH in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route2(test)