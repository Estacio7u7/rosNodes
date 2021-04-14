#!/usr/bin/env python
# necessary line to use python


import rospy
# always necessary to use nodes

from std_msgs.msg import String
# import from standard messages libraries everything needed. In this case a string message

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    #initialization of the node
    rospy.init_node('listener', anonymous=True)
    # receiving information, this executes the "callback" function, there
    # you can use the incoming information
    rospy.Subscriber('chatter', String, callback)

    # keep the node executing in loop
    rospy.spin()

if __name__ == '__main__':
    listener()
