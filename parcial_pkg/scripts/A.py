#!/usr/bin/env python

import rospy # to use ros nodes, its necessary
import random # to create random numbers
import numpy as np
from random import seed
from random import randint

from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from std_msgs.msg import Float32
seed(1)
boolPublish=False
intPublish=0
floatPublish=0.0
def strArd(strComing):
    global boolPublish
    global intPublish
    global floatPublish

    info=strComing.data
    values=info.split('/')
    c=len(values)

    for x in range(c):
        fv=values[x]
        if fv.split(':')[0] == 'bool':
            if fv.split(':')[1]== '1':
                boolPublish=(bool(1))
            else:
                boolPublish=(bool(0))
        if fv.split(':')[0] == 'int':
            intPublish=int(fv.split(':')[1])
        if fv.split(':')[0] == 'float':
            floatPublish=float(fv.split(':')[1])

def anode(): #start the function
    #global variables for incoming data
    global boolPublish
    global intPublish
    global floatPublish
    # instance the publisher
    pubBool = rospy.Publisher('A2B', Bool, queue_size=10)
    pubInt = rospy.Publisher('A2C', Int32, queue_size=10)
    pubFloat = rospy.Publisher('A2D', Float32, queue_size=10)

    # initialize the node
    rospy.init_node('anode', anonymous=False)

    # Frequency to publish
    rate = rospy.Rate(10)

    # action of publishing
    while not rospy.is_shutdown():

        # the subscribe action
        rospy.Subscriber('ard2A', String, strArd)

        # the publishing action
        # for log
        rospy.loginfo(str(boolPublish)+" "+str(intPublish)+" "+str(floatPublish))

        # for bool
        pubBool.publish(boolPublish)

        # for int
        pubInt.publish(intPublish)

        # for float
        pubFloat.publish(floatPublish)

        # to wait for the frequency
        rate.sleep()

if __name__ == '__main__': #main action of the nodes
    anode() # call the function
