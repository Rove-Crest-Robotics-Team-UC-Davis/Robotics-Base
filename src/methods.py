# import libraries.
import rospy
from std_msgs.msg import String
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
class sender:
    node = None
    pub = None
    def __init__(self, send_to):
        # create a publisher to send messages to the given topic
        pub = rospy.Publisher(send_to, String, queue_size=20)
        
        pass
    
    def send(self, message):
        # send the given message to the topic given in the constructor

        pass

class reader:
    # create object properties -- sender and reader
    node = None
    def __init__(self, get_from):
        # create a listener to read messages from the given topic

        # initialize both of the above
        pass

    def get_next(self, index):
        # return the 'index'th command from the aforementioned array.
        pass