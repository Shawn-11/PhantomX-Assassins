######################## Pyricks library ########################
from pybricks.parameters import Color, Direction, Stop, Icon, Button
from pybricks.tools import wait, StopWatch
from ACL_FLL_v04_test import *

################## Shared and local constants ##################

# Adapter configuration: (LeftPower, RightPower, LeftLimit, RightLimit)
ROUTE_ADAPTER_POWER = (40, 40, 30, 30)

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

def Route4a(laura: Laura): # 21 sec

    print("\n--- Starting Route 4 ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    laura.wall_square()
    laura.gyro_acc(power= 80 , distance= 730 , stop= False)
    laura.line_follow_degree(direction= 1 , power= 50 ,port= LEFT_COLOUR ,degree= 80 , stop= False)

    laura.line_follow_detect_reflected(direction= 1 , power= 60 ,port= LEFT_COLOUR , detect_port= RIGHT_COLOUR , threshold= 15  , stop= False)
    laura.line_follow_degree(direction= 1 , power= 50 ,port= LEFT_COLOUR ,degree= 100 , stop= False)
    laura.gyro_acc(power= 70 , distance= 130)
    # # wait(200)
    laura.gyro_lock_turn(RIGHT_DRIVE, 90)
    laura.line_follow_degree(direction= -1 , power= 40 ,port= RIGHT_COLOUR ,degree= 130 )
    laura.adapter_motor_seconds(port= RIGHT_ADAPTER , speed= -400 , duration= 1000 , wait_complete= False)

    laura.gyro_lock_turn(port= RIGHT_DRIVE , angle= 45 , stop= False)
    laura.gyro_acc(power= 60 , distance= 90 , angle= 45 )
    laura.adapter_motor_seconds(port= RIGHT_ADAPTER , speed= 1000 , duration= 1000)
    laura.encoder_time(left_power= 50 , right_power= -45  , duration= 500 )
    laura.gyro_acc(power= -80 , distance= 140 , angle= 75)
    laura.gyro_point_turn(angle= 0)
    laura.gyro_acc(power= -80 , distance= 167 )
    laura.gyro_point_turn(angle= 90)
    laura.gyro_acc(power= -80 , distance= 100 , angle= 90 , stop= False )
    laura.gyro_time(power= -50 , duration= 500 , angle= 90)
    laura.adapter_motor_seconds(LEFT_ADAPTER, -1000, 1300)
    laura.adapter_motor_seconds(LEFT_ADAPTER, 1000, 600, Stop.COAST, False)
    wait(200)
    laura.gyro_acc(power= 80 , distance= 200 , angle= 90 , stop= False)
    laura.gyro_point_turn(angle= -10 , stop= False)
    laura.gyro_acc(power= 80 , distance= 900, angle= -10, stop= False)
    # laura.gyro_acc(60, 110, -90)
    laura.gyro_point_turn( angle= -90)

    """ Route end """
    elapsed_time = routeTimer.time() / 1000
    print(f"Total Time: {elapsed_time:.2f} seconds")
    print("--- Route 4 Complete ---")

def Route4(laura: Laura): # 16 sec

    print("\n--- Starting Route 4a ---")
    routeTimer = StopWatch()
    laura.port_view_battery()
    routeTimer.reset()
    laura.hub_status_light(Color.MAGENTA)

    """ Start your code here """
    laura.wall_square()
    laura.gyro_acc(power= 80 , distance= 730 , stop= False)
    laura.line_follow_degree(direction= 1 , power= 50 ,port= LEFT_COLOUR ,degree= 80 , stop= False)
    laura.line_follow_detect_reflected(direction= 1 , power= 50 ,port= LEFT_COLOUR , detect_port= RIGHT_COLOUR , threshold= 30)
    laura.encoder_degree(left_power= 70 , right_power= -70 , degree= 170)
    laura.gyro_acc(power= -80 , distance= 100 , angle= 90 , stop= False )
    
    laura.gyro_time(power= -40 , duration= 500 , angle= 90)
    laura.adapter_motor_seconds(port= LEFT_ADAPTER , speed= -1000 , duration= 1800)
    laura.adapter_motor_seconds(port= LEFT_ADAPTER , speed= 1000 , duration= 600)
    laura.gyro_sensor(power= 50 , port= LEFT_COLOUR , threshold= 15 , angle= 90)


    laura.adapter_motor_seconds(port= RIGHT_ADAPTER , speed= -1000 , duration= 800 , wait_complete= False )
    laura.gyro_lock_turn(port= RIGHT_DRIVE , angle= 47 )
    laura.gyro_acc(power= 60 , distance= 280 , angle= 47 )
    laura.adapter_motor_seconds(port= RIGHT_ADAPTER , speed= 1000 , duration= 1000)
    laura.encoder_time(left_power= 50 , right_power= -45  , duration= 500 )


    laura.encoder_degree(left_power= -70 , right_power= 70 , degree= 230 , stop= False)
    laura.gyro_acc(power= 80 , distance= 330 , angle= -30 , stop= False)
    laura.gyro_acc(power= 80 , distance= 380)
    # laura.gyro_point_turn(angle= -87)


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
