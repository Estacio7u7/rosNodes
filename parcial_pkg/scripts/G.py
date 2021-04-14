#!/usr/bin/env python
import re # for extract numbers from a string
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
    spt3=strSplit[2].split(':')
    if spt1[1] >= spt2[1]:
        if spt1[1] >= spt3[1]:
            newMsg = spt1[0]
        else:
            newMsg = spt3[0]
    else:
        if spt2[1] >= spt3[1]:
            newMsg = spt2[0]
        else:
            newMsg = spt3[0]

    if newMsg=="High":
        newMsg="H"
    elif newMsg=="Medium":
        newMsg="M"
    else:
        newMsg="L"

def gnode():
	global newMsg
	# instance the Publisher
	pub = rospy.Publisher('G2H',String, queue_size=10)

	# initialize the node
	rospy.init_node('gnode', anonymous=False)

	# adjust the frequency
	rate = rospy.Rate(0.5)

	while not rospy.is_shutdown():
		# action of subscribing - receving data
		rospy.Subscriber('D2G',String, callback)

		# action of publishing
		pub.publish(newMsg)
		rospy.loginfo(newMsg)

		# wait for 0.5 Hz
		rate.sleep()

if __name__ == '__main__':
    gnode()
