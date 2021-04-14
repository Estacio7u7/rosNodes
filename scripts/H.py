#!/usr/bin/env python
# necessary line to use python

import rospy
# always necessary to use nodes

from std_msgs.msg import String
# import from standard messages libraries everything needed. In this case a string message
boolData=""
intData=""
floatData=""
outPut=""

def boolR(bLevel):
    global boolData
    boolData=bLevel.data
def intR(intLevel):
    global intData
    intData=intLevel.data
def floatR(floatLevel):
    global floatData
    floatData=floatLevel.data
def outDec():
    global boolData
    global intData
    global floatData
    global outPut

    # if all variables are equal, the outPut is the variables value
    if boolData == 'H':
        if intData == 'H':
            if floatData == 'H':outPut='H'
            elif floatData == 'M':outPut='H'
            elif floatData == 'L':outPut='M'
        elif intData == 'M':
            if floatData == 'H':outPut='H'
            elif floatData == 'M':outPut='M'
            elif floatData == 'L':outPut='M'
        elif intData == 'L':
            if floatData == 'H':outPut='M'
            elif floatData == 'M':outPut='M'
            elif floatData == 'L':outPut='L'

    elif boolData == 'L':
        if intData == 'H':
            if floatData == 'H':outPut='H'
            elif floatData == 'M':outPut='M'
            elif floatData == 'L':outPut='M'
        elif intData == 'M':
            if floatData == 'H':outPut='M'
            elif floatData == 'M':outPut='M'
            elif floatData == 'L':outPut='L'
        elif intData == 'L':
            if floatData == 'H':outPut='M'
            elif floatData == 'M':outPut='L'
            elif floatData == 'L':outPut='L'
def hnode():
    global outPut
    #instance the publish nodes
    pub= rospy.Publisher('H2Ard', String, queue_size=10)
    #initialization of the node
    rospy.init_node('hnode', anonymous=False)
    # adjust the frequency
    rate = rospy.Rate(0.2)
    # receving information and processing in callback
    while not rospy.is_shutdown():
		# action of subscribing - receving data
        rospy.Subscriber('E2H', String, boolR)
        rospy.Subscriber('F2H', String, intR)
        rospy.Subscriber('G2H', String, floatR)
        outDec()
		# action of publishing
        pub.publish(outPut)
        rospy.loginfo(outPut)
		# wait for 0.5 Hz
        rate.sleep()

if __name__ == '__main__':
    hnode()
