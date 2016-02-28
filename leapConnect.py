###############################################################################
# This script prints out hand information to the terminal using the Leap SDK python API.
# Before running, you will have to download the python.Framework from https://www.python.org/downloads/ (Not sure if this is the same on Windows)
# The folder you run from must conatin leapConnect.py, Leap.py, LeapPython.so, and libLeap.dylib (for Mac) (Leap.dll for Windows)
# To run type 'python leapConnect.py' into the terminal. (I think for windows you'll need to download a terminal emulator)

import os, sys, inspect, thread, time, Leap

class Listener(Leap.Listener):

    def on_connect(self, controller): # Confirm connection to Leap Motion Controller
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

            print "  %s, gripper: %s, (x, y, z): %s" % (
                handType, gripper, hand.palm_position) # Show Left/Right hand and x,y,z position for each frame

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

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
