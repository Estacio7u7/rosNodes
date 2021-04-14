#!/usr/bin/env python

import rospy #for using nodes
from std_msgs.msg import Int32 # to use the int in this node
from std_msgs.msg import String

#global variable
newMsg=""

def callback(intVariable):
    global newMsg
    # getting back the variable
    intData=int(intVariable.data)

	# evaluating for fuzzy values of integers values
    if intData <= 80:
        newMsg='Low: 100% / Medium: 0% / High: 0%'

    if intData > 80 and intData <= 90:
        lowValue=-10*intData+900
        middValue=10*intData-800
        newMsg= "Low:" + str(lowValue) + "%/ Medium: " + str(middValue) + "%/ High: 0%"

    if intData>90 and intData <=165:
        newMsg='Low: 0% / Medium: 100% / High: 0%'

    if intData > 165 and intData <= 175:
        middValue=-10*intData+1750
        highValue=10*intData-1650
        newMsg= "Low: 0%/ Medium:" + str(middValue) + "%/ High: " + str(highValue) + "%"

    if intData > 175:
        newMsg = 'Low: 0% / Medium: 0% / High: 100%'


def cnode():
	global newMsg
	# instance the Publisher
	pub = rospy.Publisher('C2F', String, queue_size=10)

	# initialize the node
	rospy.init_node('cnode', anonymous=False)

	# adjust the frequency
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		# action of subscribing - receving data
		rospy.Subscriber('A2C', Int32, callback)

		# action of publishing
		pub.publish(newMsg)
		rospy.loginfo(newMsg)

		# wait for 1 Hz
		rate.sleep()

if __name__ == '__main__':
    cnode()
