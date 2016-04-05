import os, sys, inspect, thread, time, Leap
from Leap import CircleGesture
class Listener(Leap.Listener):
    state_names=['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_connect(self, controller): # Confirm connection to Leap Motion Controller
    	controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        print "Test to ensure Leap Motion is connected: "
        print "\t PASSED: Connected"

    def on_disconnect(self, controller):
        print "Test to ensure program knows when Leap Motion is disconnected:"
        print "\t PASSED: Disconnected"

    def on_exit(self, controller): # Pressing 'enter' will exit script
        print "Test to ensure user has exited the program:"
        print "\t PASSED: Exited"




def main():

    print "Tests to be run: \n \tPlug Leap Motion in to pass connect test. \n \t Unplug Leap Motion to pass disconnect to pass disconnect test. \n \t Press enter to pass program exit test"
    # Create a listener and controller
    listener = Listener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
