"""
Flies the Anafi in a fairly wide arc.  You want to be sure you have room for this. (it is commented
out but even what is here is still going to require a large space)

Author: Amy McGovern
"""
from pyparrot.Anafi import Anafi
import math

Anafi = Anafi()

print("connecting")
success = Anafi.connect(10)
print(success)

print("sleeping")
#Anafi.smart_sleep(5)

Anafi.ask_for_state_update()

#print("Flying direct: going forward (positive pitch)")
#Anafi.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)

#print("Flying direct: yaw")
#Anafi.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=1)

#print("Flying direct: going backwards (negative pitch)")
#Anafi.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)

#print("Flying direct: roll")
#Anafi.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=1)

#print("Flying direct: going up")
#Anafi.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

#print("Turning relative")
#Anafi.move_relative(0, 0, 0, math.radians(90))

# this works but requires a larger test space than I currently have. Uncomment with care and test only in large spaces!
#print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
#Anafi.fly_direct(ro
#

try:
    print("TAKE OFF")
    Anafi.safe_takeoff(5)

    #Anafi.start_video_stream()
    print("UP")
    Anafi.fly_direct(roll=0, pitch=-15, yaw=0, vertical_movement=75, duration=2)
    #Anafi.fly_direct(roll=0, pitch=25, yaw=0, vertical_movement=0, duration=1.5)

    print("WAIT")
    Anafi.smart_sleep(5)

    # print("FORMAT")
    # set_picture_format()
    print("PICTURE")
    Anafi.take_picture()
    
    #Anafi.fly_direct(roll=-0, pitch=-0, yaw=0, vertical_movement=0, duration=1)

    #Anafi.fly_direct(roll=-5, pitch=-45, yaw=0, vertical_movement=0, duration=2)
    print("DOWN")
    Anafi.fly_direct(roll=0, pitch=-15, yaw=0, vertical_movement=-25, duration=2)
    #Anafi.stop_video_stream() 

    #Anafi.fly_direct(roll=15, pitch=0, yaw=0, vertical_movement=0, duration=2)
    #Anafi.fly_direct(roll=-25, pitch=0, yaw=0, vertical_movement=0, duration=2)
    #Anafi.fly_direct(roll=0, pitch=10, yaw=50, vertical_movement=0, duration=2)
    print("PASSED")
    Anafi.safe_land(5)
except:
    print("FAILED")
    Anafi.safe_land(5)
print("DONE - disconnecting")
Anafi.disconnect()