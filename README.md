# rosNodes
  This scripts are part of a practice to being started on the ROS nodes topic. Practice with three "flavors" of nodes and arduino comunication. All documentation has been taken from ROS web page and can be found there.  Strongly recomend install Arduino first and the arduino ros serial node to work with it.

Structure of this practice
==============

Nodes are the hearth of working in ROS. Everything we can do in ROS mainly goes into a node. Here we have nine Nodes that receives, processes and sends information, with different frequencys and making a work with Arduino.

> this is a class exercise, not necessary to explain everything here. For more information every code is commented.

Definitions
=============

- **Topics** A topic is a channel of information that goes from one Node to another. It has two properties: name and type.
- **Publisher** Is the node that sends information.
- **Subscriber** Is the node or nodes that receives the information.

The Work
===========

1. We have an Arduino card connected to two analog inputs and a discrete one; Additional, we have an analog Output, anything that let us see a change in the value.
2. We start the eight nodes written in python one by one inside the ROS environment
3. we start the ROS serial arduino node. You can check the documentation here <http://wiki.ros.org/rosserial_arduino>
4. Check that, when you change a value in the INPUTS, it's not obvious the output value due to a Net inside the ROS structure. You can check the net with the command on the prompt:

``` 
rqt_graph
```

<!-- This will open the graphic interface of ros. For an easier visualization stop the ROS serial arduino node and refresh the graphic. Keep the Debug marked.-->
