# import libraries.
import rospy
from std_msgs.msg import String
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
class sender:
    pub = None
    def __init__(self, send_to):
        # create a publisher to send messages to the given topic
        pub = rospy.Publisher(send_to, String, queue_size=20)
    
    def send(self, message):
        # send the given message to the topic given in the constructor
        pub.publish(message)
        rospy.loginfo(message)
        

class reader:
    # create object properties -- sender and reader
    pub = None
    def __init__(self, get_from):
        # create a listener to read messages from the given topic

        # initialize both of the above
        pass

    def get_next(self, index):
        # return the 'index'th command from the aforementioned array.
        pass