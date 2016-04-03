###############################################################################
# This script prints out hand information to the terminal using the Leap SDK python API.
# Before running, you will have to download the python.Framework from https://www.python.org/downloads/ (Not sure if this is the same on Windows)
# The folder you run from must conatin leapConnect.py, Leap.py, LeapPython.so, and libLeap.dylib (for Mac) (Leap.dll for Windows)
# To run type 'python leapConnect.py' into the terminal. (I think for windows you'll need to download a terminal emulator)

import os, sys, inspect, thread, time, Leap
from leap import CircleGesture
class Listener(Leap.Listener):
    state_names=['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_connect(self, controller): # Confirm connection to Leap Motion Controller
    	controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        print "Connected"


    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller): # Pressing 'enter' will exit script
        print "Exited"

    def on_frame(self, controller): # Get the most recent frame and report some basic information
        frame = controller.frame()

        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers.extended()))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            if (len(frame.fingers.extended()) == 0):
                gripper = "closed"
            else:
                gripper = "open"

            x = hand.palm_position[0]
            y = hand.palm_position[1]
            z = hand.palm_position[2]

            normal = hand.palm_normal
	    
            print "  %s, gripper: %s, Position: (%s, %s, %s), Normal Vector: %s" % (
                handType, gripper, x, y, z, normal) # Show Left/Right hand and x,y,z position for each frame
                
            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction
            
            #pitch=rotation around x-axis
	    #yaw=rotation around y-axis
	    #roll=rotation around z-axis
	    print "Pitch: " +str(direction.pitch*Leap.RAD_TO_DEG) + "Yaw: " +str(direction.yaw*Leap.RAD_TO_DEG) + "Roll: " +str(normal.roll*Leap.RAD_TO_DEG)
	    
    def on_device_change(self, controller):
	       print "Device change"

    def on_device_failure(self, controller):
	       print "Device failed"
	       
    gesture_list = frame.gestures(start_frame)
    for gesture in frame.gestures();
    	if gesture.type==Leap.Gesture.TYPE_CIRCLE
    		circle=CircleGesture(gesture)
    		if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
    			clock="clockwise"
    		else:
    			clock="counter-clockwise"
    		swept_angle=0
    		if circle.state != Leap.Gesture.STATE_START #if state of circle isn't start state
    		#calculate angle that has been swept out by drawing circle
    		previous= CircleGesture(controller.frame(1).gesture(circle.id))
    		swept_angle= (cirle.progress - previous.progress) * 2 * Leap.PI
    		print "ID: " + str(circle.id) + "Swept angle: " +str(swept_angle * Leap.RAD_TO_DEG) + " " + clock
	        

def main():
    # Create a listener and controller
    listener = Listener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
