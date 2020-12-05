# import libraries.
import rospy
from std_msgs.msg import String
import static_data as data
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
    r_index = -1
    def set_reader_data(string):
        data.reader_data[r_index] = string

    def __init__(self, get_from, reader_index):
        r_index = reader_index
        # create a listener to read messages from the given topic
        pub = rospy.Subscriber(get_from, String, set_reader_data)

    def get_next(self):
        # return the next command.
        return data.reader_data[r_index]