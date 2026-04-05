######################## Pyricks library ########################
from pybricks.parameters import Color, Direction, Stop, Icon, Button
from pybricks.tools import wait, StopWatch
from ACL_FLL_v04_test import *

################## Shared and local constants ##################

# Adapter configuration: (LeftPower, RightPower, LeftLimit, RightLimit)
ROUTE_ADAPTER_POWER = (-40, -40, 30, 30)

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

def Route1(laura):

    print("\n--- Starting Route 1 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    # Step 1 - Go to market
    laura.wall_square()
    laura.gyro_acc(power= 60 , distance= 80 , angle= 0 , decel_dist=0 , stop=False) 
    laura.move_curve_angle(20,-42,500,600,Stop.BRAKE,100)
    laura.gyro_acc(power= 85 , distance= 280 , angle= -43 , decel_dist=0 , stop=False)
    laura.gyro_time(power= 55 , duration= 820 , angle= -43)

    # Step 2 - Solve mission
    laura.adapter_motor_seconds(LEFT_ADAPTER,speed= 600 , duration= 800, stop_method=Stop.COAST, wait_complete=False)
    laura.adapter_motor_seconds(RIGHT_ADAPTER, speed= 400 , duration= 1000 , stop_method=Stop.HOLD)


    # Step 3 - Pull market back
    laura.gyro_time(-60,450,angle=-44)
    laura.adapter_motor_seconds(RIGHT_ADAPTER,speed= -850 , duration= 700, stop_method=Stop.HOLD, wait_complete=False)
    laura.adapter_motor_seconds(LEFT_ADAPTER, speed= -550 , duration= 600, wait_complete=False)
    wait(700)

    # Step 4 - Back to base
    laura.gyro_acc(power= -80 , distance= 200 , angle= -44 , accel_dist=80,decel_dist= 0 , stop= False)
    # laura.gyro_point_turn(angle= -90 , stop= False, accel_dist= 0 , decel_dist= 0)
    laura.gyro_acc(power= -80 , distance= 200 , angle= -90 , accel_dist=80,decel_dist=0 , stop= False)
    # laura.gyro_point_turn(angle= 0 , stop= False, accel_dist= 0, decel_dist= 0)
    laura.gyro_acc(power= -80 , distance= 170 , angle= 0 , accel_dist= 80,decel_dist= 30)


    # laura.gyro_point_turn(angle= 75 , stop= False)
    # laura.encoder_time(left_power= 60 ,right_power= 60 , duration= 400)



    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 1 Complete ---")

######################## Route testing ########################

# For individual route testing only.
if __name__ == "__main__":
    test = Laura()

    while not Button.BLUETOOTH in test.hub_button_pressed():
        test.unregulated_adapter(*ROUTE_ADAPTER_POWER)
    
    test.adapter_motor_brake(LEFT_ADAPTER)
    test.adapter_motor_brake(RIGHT_ADAPTER)

    Route1(test)
