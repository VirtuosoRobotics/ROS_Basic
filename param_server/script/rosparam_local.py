#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    pub = rospy.Publisher('send_param', String, queue_size=10)
    rospy.init_node('rosparam_test', anonymous=False)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        sending_msg = rospy.get_param('~input','nothing')
        msg = String()
        msg.data = sending_msg
        pub.publish(msg)
        print msg
        rate.sleep()
