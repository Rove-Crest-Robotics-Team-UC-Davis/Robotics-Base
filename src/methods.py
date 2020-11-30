# import libraries.
import rospy

class handler:
    # create object properties -- sender and reader

    def __init__(self, send_to, get_from):
        # create a publisher to send messages to the given topic

        # create a listener to read messages from the given topic

        # initialize both of the above
        pass

    def send(self, message):
        # send the given message to the topic given in the constructor
        pass

    def create_reader(self):
        # recieve data and add it to the array of commands from IK
        pass
    def get_command(self, index):
        # return the 'index'th command from the aforementioned array.
        pass
    def done_command(self, index):
        # remove the command of the given index from the array.
        pass