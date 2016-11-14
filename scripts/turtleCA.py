#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callbackSubscriber(twistData):
    rospy.loginfo("x = %f" % twistdata.linear.x)
    twistdata.linear.x = -twistdata.linear.x
    rospy.loginfo("x = %f" % twistdata.linear.x)
    pub = rospy.Publisher('cmd_vel_CA', Twist, queue_size=1)
    pub.publish(twistData)

def turtleCA():
    rospy.init_node('turtleCA', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callbackSubscriber)
    pub = rospy.Publisher('cmd_vel_CA', Twist, queue_size=1)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        turtleCA()
    except rospy.ROSInterruptException:
        pass
