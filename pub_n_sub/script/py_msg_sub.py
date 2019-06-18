#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pub_n_sub.msg import Num

def callback(data):
    print data
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("custom_msg", Num, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()