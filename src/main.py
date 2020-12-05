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
pub_node = handler.__init__('reqd_pos', ['curr_pos', 'IK_in'])

while True:
    # Listen to IK's program's publishing node and store it in a local variable

    # Listen to Ardunio's publishing node and store the string onto a variable.

    # while the robot arm's position is not equal to last sent, wait.

    # Send the message from IK to arduino

    # Update the last sent variable.
    pass  