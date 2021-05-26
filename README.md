# rosNodes
  This scripts are part of a practice to being started on the ROS nodes topic. Practice with three "flavors" of nodes and arduino comunication. All documentation has been taken from ROS web page and can be found there.  Strongly recomend install Arduino first and the arduino ros serial node to work with it.

Structure of this practice
==============

Nodes are the hearth of working in ROS. Everything we can do in ROS mainly goes into a node. Here we have nine Nodes that receives, processes and sends information, with different frequencys and making a work with Arduino.

<!--[nodes](https://user-images.githubusercontent.com/82511885/119656417-4ad1db80-bdf0-11eb-9917-d532dfc4e4ba.jpeg)-->
<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/82511885/119656417-4ad1db80-bdf0-11eb-9917-d532dfc4e4ba.jpeg">
</p>

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

The scripts explained
===========

**Script A.py: The node A**
This node begins the data reception from Arduino board, establishes the subscriber for serial comunication and detects the variables and values tha arduino sends. The next type of variables are recepted in a string component:
- **Bool:** This one corresponds to a TRUE/FALSE value. In our circuit, we use a simple pulse button that makes a ON/OFF jump.
- **Int:** This one goes from 0 to 1023 and is the value that Arduino board provides from the ADC. In our circuit we used a simple potentiometer connected between 0 and 5v.
- **Float:** This one goes from 0 to 5 with decimals that is the advantage of float numbers. Corresponds to another potentiometer connected in the same way that the previous one. 

These values are sent to nodes B, C and D separately and simoultaneosly with a frequenzy of 0.1Hz.

**Scripts B.py, C.py, D.py: The nodes B,C and D**
This nodes processes the recepted values by aplying a simple fuzzy logic inside every node. The node B has only two values otherwise C and D, that has three. After fuzzyfication, they send a string with the level that those values belongs to in percentaje. As an example you would this this output in C or D node:

```
LOW: 10% / MEDIUM: 90% / HIGH: 0%
```
In the A node the output is simplier:

```
LOW: 0% / HIGH: 100%
```
This information is processed and sent to the next layer of nodes with a frequenzy of 1Hz

**Scripts E.py, F.py, G.py: The nodes E,F and G**
This nodes separates the string sent by the previous nodes layer an makes a decition tree to choose wich level actually the value corresponds to.To make it simple, we made that value goes directly for the segment that the biggest percentage belongs to and sent the first letter of its name.
As example, for the imput:
```
LOW: 45% / MEDIUM: 55% / HIGH: 0%
```
You would see an output like this:
```
M
```
This information is processed and sent to the next layer of nodes with a frequenzy of 0,5Hz

**Script H.py: The defuzzyficator node H**
This node makes a decition tree that converts those three values in a only one that is being sent to the Arduino Board as a String every 5 seconds or with a frequenzy of 5Hz.

**Arduino Scipt: The board as I/O interface**
We connected two potenciometers as analog inputs and a button as digital input. To see the result we connected a difuse led that changes its brightness taking advantages of PWM pins. The script creates a node that sends a string to the A node with values processed from the connected pins.
As example, you would see the following:

```
Bool: TRUE / Int:655 / Float: 3.7
```

# Developed by: 
- Luis Carlos Parra Camacho
- Juan Andrés Alzate Ocampo
- Andrés Fernando Rodríguez Bayona
- Amy Alexandra Noriega Quintero
- David Fernando Estacio Quiroz.
