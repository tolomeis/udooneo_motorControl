#!/usr/bin/env python

import rospy
from neo import easyGpio
from geometry_msgs.msg import Twist
import subprocess
import serial

#set output enable
En1 = easyGpio(20)
En2 = easyGpio(21)
En3 = easyGpio(22)
En4 = easyGpio(19)
En1.pinOUT()
En2.pinOUT()
En3.pinOUT()
En4.pinOUT()

arduino = serial.Serial('/dev/ttyMCC', 115200, timeout=1)

def callback(velMsg):
	rospy.loginfo("topic value:" +str(velMsg.linear.x)+str(velMsg.angular.z))
	vdx = (1+velMsg.linear.x)*50
	vsx = vdx
	vdx += velMsg.angular.z*50
	vsx -= velMsg.angular.z*50
	vsx = min(256, max(0, vsx))
	vdx = min(256, max(0, vdx))
	
	rospy.loginfo("requested: "+str(vdx)+" "+str(vsx))
	arduino.write(bytes(str(int(vdx))+","+str(int(vsx))+","))
	ack = arduino.readline()
	rospy.loginfo(ack)

def listen():
	#enable motors
	En1.off()
	En2.off()
	En3.off()
	En4.off()

	#init ROS node
	rospy.init_node('udoo_motor_controller', anonymous=False)
	rospy.Subscriber("cmd_vel", Twist, callback)
	rospy.loginfo("started")
	rospy.spin()

if __name__ == '__main__':
	listen()
