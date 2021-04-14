#!/usr/bin/env python
# necessary line to use python


import rospy
# always necessary to use nodes

from std_msgs.msg import String
# import from standard messages libraries everything needed. In this case a string message

#global variables to interchange information betwenn objects
incomeMessage = "" # An empty string to ve filled with incoming information

# the callabck function, here you can use the incoming information
def callback(information):
	global incomeMessage
	incomeMessage= information.data

	# what do you want to do with the incoming information?
	#
	#
	####################################################


def carrier():
	# use the global variable
	global incomeMessage

	#instance the emmiter node
	pub = rospy.Publisher(' stringPublishingTopicName ', String, queue_size=10)
	# emmiter frequency
	rate = rospy.Rate(10)

	# initialice the node
	rospy.init_node('carrier', anonymous=True/False)


	# loop for the execution of the node
	while not rospy.is_shutdown():
		# first subscribe to a node that is needed to receive information from
		rospy.Subscriber('topicSubscribingNode', String, callback)

		# second, publish the information we rescued and treated on callback
		pub.publish(incomeMessage)
		rospy.loginfo(incomeMessage)

		# ensure the frequency of the node
		rate.sleep()

if __name__ == '__main__':
	carrier()
