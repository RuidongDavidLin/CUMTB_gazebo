#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def cmd_callback(data):
  
  global pub

  if data.angular.z != 0 : 
    twist = Twist()
    twist.linear.x = data.linear.x 
    twist.linear.y = data.linear.y 
    twist.linear.z = data.linear.z
    twist.angular.x = data.angular.x
    twist.angular.y = data.angular.y
    twist.angular.z = data.angular.z
    pub.publish(twist)
  else:
    twist = Twist()
    twist.linear.x = data.linear.x + 0.5
    twist.linear.y = data.linear.y 
    twist.linear.z = data.linear.z
    twist.angular.x = data.angular.x
    twist.angular.y = data.angular.y
    twist.angular.z = data.angular.z
    pub.publish(twist)



if __name__ == '__main__':
    try:
      rospy.init_node('race_optimize_controller')

      rospy.Subscriber('/vel', Twist, cmd_callback, queue_size=1)
      pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

      rospy.spin()
    except rospy.ROSInterruptException:
        pass

