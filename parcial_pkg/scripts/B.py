#!/usr/bin/env python

import rospy #for using nodes
from std_msgs.msg import Bool # to use the bool in this node
from std_msgs.msg import String

#global variable
newMsg=""

def callback(boolVariable):
	global newMsg
	# getting back the variable
	boolData=boolVariable.data

	# deciding for an option
	if boolData==True:
		newMsg='High:100%/Low:0%'
	else:
		newMsg='High:0%/Low:100%'

def bnode():
	global newMsg
	# instance the Publisher
	pub = rospy.Publisher('B2E', String, queue_size=10)

	# initialize the node
	rospy.init_node('bnode', anonymous=False)

	# adjust the frequency
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		# action of subscribing - receving data
		rospy.Subscriber('A2B', Bool, callback)

		# action of publishing
		pub.publish(newMsg)
		rospy.loginfo(newMsg)

		# wait for 1 Hz
		rate.sleep()

if __name__ == '__main__':
    bnode()
