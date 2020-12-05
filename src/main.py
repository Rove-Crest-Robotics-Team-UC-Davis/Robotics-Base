#!/usr/bin/env python
# This file is the master for ROS handler
# importing libararies
import rospy
from std_msgs.msg import String
from methods import *

# initialize a variable to store the last sent value
last_sent = ""
# Create a ros publisher node 'reqd_pos' (that sends Strings)
# queue size --> the number of messages that this topic must store as a backlog. 
reqd_pos = sender.__init__('reqd_pos')
curr_pos = reader.__init__('curr_pos')
ik_in = reader.__init__('ik_in')

while not rospy.is_shutdown():
    # Listen to IK's program's publishing node and store it in a local variable
    from_ik = ik_in.get_next()
    # Listen to Ardunio's publishing node and store the string onto a variable.
    from_ard = curr_pos.get_next()
    while not (from_ard == from_ik):
        from_ard = curr_pos.get_next()
    # while the robot arm's position is not equal to last sent, wait.

    # Send the message from IK to arduino

    # Update the last sent variable.
    pass  