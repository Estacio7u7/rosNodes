#!/usr/bin/env python

import rospy #for using nodes
from std_msgs.msg import String

#global variable
newMsg=""

def callback(stringData):
	global newMsg
	# getting back the variable
	stringComming=stringData.data
	# looking for data
	strSplit=stringComming.split('/')
	spt1=strSplit[0].split(':')
	spt2=strSplit[1].split(':')
	if spt1[1] == '100%':
		newMsg=spt1[0]
	else:
		newMsg=spt2[0]
	if newMsg == 'High':
		newMsg='H'
	else:
		newMsg='L'
def enode():
	global newMsg
	# instance the Publisher
	pub = rospy.Publisher('E2H',String, queue_size=10)

	# initialize the node
	rospy.init_node('enode', anonymous=False)

	# adjust the frequency
	rate = rospy.Rate(0.5)

	while not rospy.is_shutdown():
		# action of subscribing - receving data
		rospy.Subscriber('B2E',String, callback)

		# action of publishing
		pub.publish(newMsg)
		rospy.loginfo(newMsg)

		# wait for 0.5 Hz
		rate.sleep()

if __name__ == '__main__':
    enode()
