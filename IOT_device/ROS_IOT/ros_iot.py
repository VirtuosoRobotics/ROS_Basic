#!/usr/bin/env python
# license removed for brevity
import cherrypy
import threading
import time
import serial
import rospy
from std_msgs.msg import *

nanoSerial = serial.Serial("/dev/ttyUSB0", 9600)
sonic_value = '0'

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    }
}

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)

    @cherrypy.expose
    def sonic(self):
        return 'ultrasonic value: ', sonic_value

def startCherry():
    cherrypy.quickstart(HelloWorld(), '/',config)

def arduino_driver():
    global sonic_value
    while True:
        serin = ''
        serin = nanoSerial.read()
        if serin == 'S':
            serin = nanoSerial.read()
            if serin == 'U':
                serin = nanoSerial.read(4)
                if serin[3] == 'E':
                    sonic_value = serin[0:3]
                    print sonic_value


def talker():
    pub = rospy.Publisher('ultrasonic', Int32, queue_size=10)
    rospy.init_node('ultrasonic', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        ultrasoinc_str = "ultrasonic %s" % sonic_value
        rospy.loginfo(ultrasoinc_str)
        pub.publish(int(sonic_value))
        rate.sleep()

if __name__ == '__main__':
    t = threading.Thread(target=startCherry)
    t.daemon = True
    t.start()

    t2 = threading.Thread(target=arduino_driver)
    t2.daemon = True
    t2.start()

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
