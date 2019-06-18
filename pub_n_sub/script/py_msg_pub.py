#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from pub_n_sub.msg import Num

def talker():
    pub = rospy.Publisher('custom_msg', Num, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Num()
        msg.first_name = "pika"
        msg.last_name = "chu"
        msg.age = 8
        msg.score = 87
        pub.publish(msg)
        print msg
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass