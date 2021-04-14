#!/usr/bin/env python 
#necessary line to use python

import rospy
#always necessary to use ros nodes 

from std_msgs.msg import String 
# import from standard messages libraries everything needed. In this case a string message

#this is the program being executed
def emitterNode():
	# instance the publisher with the topic to publish, type of the topic and the permanent queue
	pub = rospy.Publisher(' stringTopicName ', String, queue_size=10) 
	
	# initialize the node, anonymous is to add a random number to the name and execute multiple same nodes
	rospy.init_node('emitterNode', anonymous=True/False) 

	#adjust the frequency 	
	rate = rospy.Rate(10)

	# loop to permanently execute an action inside the node
	while not rospy.is_shutdown():

	# actions to be maked
	#
	#
        
	# publish the information
		# to terminal and log
	rospy.loginfo(hello_str) 
		# to the topic
        pub.publish("information")

	# wait to complete the frequency
        rate.sleep() 

#this is the main program
if __name__ == '__main__': 
	emitter()

