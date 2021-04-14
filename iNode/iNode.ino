#include <ros.h>
#include <std_msgs/String.h>

// comando para correr el nodo de arduino en la terminal
// rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600
// comando para dar permisos a arduino
// sudo chmod 777 /dev/ttyACM0

int intValue=0;
float floatValue=0.0;
bool boolValue=false;
String dt2snd="";
char msg[30];

ros:: NodeHandle arduinoNode; // handle for the arduino node
std_msgs::String msg4ROS; // new variable type string for ROS

ros::Publisher arduControl( "ard2A", &msg4ROS); // publisher node name is arduControl
                        // and ard2A is the topic, the msg4ROS is the variable to publish
   
void msgRecep(const std_msgs::String& msgComming)
{
  if((String)msgComming.data == "L")
  {
    analogWrite(9, 25);  
  }
  if((String)msgComming.data == "M")
  {
    analogWrite(9, 127);  
  }
  if((String)msgComming.data == "H")
  {
    analogWrite(9, 255);  
  }
}

ros::Subscriber<std_msgs::String> sub("H2Ard", msgRecep);

void setup() {
  pinMode(9, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  arduinoNode.initNode(); // initialize the node on arduino board
  arduinoNode.advertise(arduControl);
  arduinoNode.subscribe(sub);
  randomSeed(analogRead(0));
}

void loop() {

  // reading values to send ROS
  intValue=map(analogRead(A0), 0, 1023, 0, 255);
  floatValue =(float)map(analogRead(A1), 0, 1023, 0, 500)*1/100.0;
  boolValue = digitalRead(A2);


  // Sending Values to ros
  dt2snd= "int:" + (String)intValue + "/float:" + (String)floatValue + "/bool:" + (String)boolValue;
  dt2snd.toCharArray(msg,30);
  msg4ROS.data =  msg;
  arduControl.publish(&msg4ROS);
  arduinoNode.spinOnce();
  delay(100);
}
