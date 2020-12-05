# import libraries.
import rospy
from std_msgs.msg import String
import static_data as data
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
 
class sender:
    pub = None
    def __init__(self, send_to):
        # create a publisher to send messages to the given topic
        self.pub = rospy.Publisher(send_to, String, queue_size=20)
    
    def send(self, message):
        # send the given message to the topic given in the constructor
        self.pub.publish(message)
        rospy.loginfo(message)
        


class reader:
    # create object properties -- sender and reader
    pub = None
    r_index = -1
    def set_reader_data(string):
        data.reader_data[self.r_index] = string

    def __init__(self, get_from, reader_index):
        self.r_index = reader_index
        # create a listener to read messages from the given topic
        self.pub = rospy.Subscriber(get_from, String, self.set_reader_data)

    def get_next(self):
        # return the next command.
        return data.reader_data[self.r_index]