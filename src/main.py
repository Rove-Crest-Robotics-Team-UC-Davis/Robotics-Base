#!/usr/bin/env python
# This file is the master for ROS handler
# importing libararies
import rospy
from std_msgs.msg import String
from methods import *

# Create a ros publisher node 'reqd_pos' (that sends Strings)
# queue size --> the number of messages that this topic must store as a backlog. 
reqd_pos = sender('reqd_pos')
curr_pos = reader('curr_pos', 0)
ik_in = reader('ik_in', 1)

# initialize a variable to store the last sent value
last_sent = ik_in.get_next()

# initalize this program as a ros node.
rospy.init_node('ROS_handler', anonymous=True)
# rospy rate for syncing the ros handler with the I/O
rate = rospy.Rate(10) # 10 hZ

def run(last_sent):
    while not rospy.is_shutdown():
        # Listen to IK's program's publishing node and store it in a local variable
        from_ik = ik_in.get_next()
        # Listen to Ardunio's publishing node and store the string onto a variable.
        from_ard = curr_pos.get_next()
        # while the robot arm's position is not equal to last sent, wait.
        while not (from_ard == last_sent):
            from_ard = curr_pos.get_next()
        
        # Send the message from IK to arduino
        reqd_pos.send(from_ik)
        # Update the last sent variable.
        last_sent = from_ik
        # wait for syncing.
        rate.sleep()

if __name__ == '__main__':
    try:
        run(last_sent)
    except rospy.ROSInterruptException:
        print("ROS has been interrupted.")