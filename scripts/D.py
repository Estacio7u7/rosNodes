#!/usr/bin/env python

import rospy #for using nodes
from std_msgs.msg import Float32 # to use the int in this node
from std_msgs.msg import String

#global variable
newMsg=""

def callback(floatVariable):
    global newMsg
    # getting back the variable
    floatData=float(floatVariable.data)
	# evaluating for fuzzy values for float Values
    if floatData <= 1.3:
        newMsg='Low: 100% / Medium: 0% / High: 0%'

    if floatData > 1.3 and floatData <= 2:
        lowValue=-142.86*floatData+285.72
        middValue=142.86*floatData-185.72
        newMsg= "Low:" + str(lowValue) + "%/ Medium: " + str(middValue) + "%/ High: 0%"

    if floatData>2 and floatData <=3:
        newMsg='Low: 0% / Medium: 100% / High: 0%'

    if floatData > 3 and floatData <= 3.6:
        middValue=-166.7*floatData+600.1
        highValue=166.7*floatData-500.1
        newMsg= "Low: 0%/ Medium:" + str(middValue) + "%/ High: " + str(highValue) + "%"

    if floatData > 175:
        newMsg = 'Low: 0% / Medium: 0% / High: 100%'

def dnode():
	global newMsg
	# instance the Publisher
	pub = rospy.Publisher('D2G', String, queue_size=10)

	# initialize the node
	rospy.init_node('dnode', anonymous=False)

	# adjust the frequency
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		# action of subscribing - receving data
		rospy.Subscriber('A2D', Float32, callback)

		# action of publishing
		pub.publish(newMsg)
		rospy.loginfo(newMsg)

		# wait for 1 Hz
		rate.sleep()

if __name__ == '__main__':
    dnode()
