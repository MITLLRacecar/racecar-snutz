"""
Copyright MIT and Harvey Mudd College
MIT License
Summer 2020
Lab 1 - Driving in Shapes
"""

########################################################################################
# Imports
########################################################################################

import sys

sys.path.insert(1, "../../library")
import racecar_core
import racecar_utils as rc_utils

########################################################################################
# Global variables
########################################################################################

rc = racecar_core.create_racecar()

# Put any global variables here
########################################################################################
# Functions
########################################################################################

def start():
    """
    This function is run once every time the start button is pressed
    """
    # Begin at a full stop
    rc.drive.stop()

    # Print start message
    print(
        ">> Lab 1 - Driving in Shapes\n"
        "\n"
        "Controls:\n"
        "    Right trigger = accelerate forward\n"
        "    Left trigger = accelerate backward\n"
        "    Left joystick = turn front wheels\n"
        "    A button = drive in a circle\n"
        "    B button = drive in a square\n"
        "    X button = drive in a figure eight\n"
        "    Y button = drive in a shape of your choice\n"
    )

def update():
    global counter 
    '''
    if rc.controller.was_pressed(rc.controller.Trigger.Right):
        print("Accelerating forward...")
        rc.drive.set_speed_angle(1,0)

    if rc.controller.was_pressed(rc.controller.Trigger.Left):
        print("Accelerating backward...")
        rc.drive.set_speed_angle(-1,0)
    '''
    if rc.controller.was_pressed(rc.controller.Button.A):
        print("Driving in a circle...")
        rc.drive.set_speed_angle(1,1)
        
    if rc.controller.was_pressed(rc.controller.Button.B):
        print("Driving in a square...")
        rc.drive.set_speed_angle(1,0)
        if counter % 4 == 0:
            rc.drive.set_speed_angle(0,1)
        rc.get_delta_time()

    if rc.controller.was_pressed(rc.controller.Button.X):
        print("Driving in an 8... ")
        rc.drive.set_speed_angle(1,1)
        rc.drive.set_speed_angle(-1,-1) 

    if rc.controller.was_pressed(rc.controller.Button.Y):
        print("Driving in an S...")
        rc.drive.set_speed_angle(1,-0.5)
        rc.drive.set_speed_angle(1,0.5)
        #rc.stop()

########################################################################################
# DO NOT MODIFY: Register start and update and begin execution
########################################################################################

if __name__ == "__main__":
    rc.set_start_update(start, update)
    rc.go()