#!/usr/bin/env python
# license removed for brevity
import cherrypy
import threading
import time
import serial
import rospy
from std_msgs.msg import *

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    }
}

pub = rospy.Publisher('rest_to_topic', String, queue_size=10)

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

    @cherrypy.expose
    def pub(self):
        msg = String()
        msg.data = 'hi'
        pub.publish(msg)
        return 'topic published'

def startCherry():
    cherrypy.quickstart(HelloWorld(), '/',config)

if __name__ == '__main__':
    t = threading.Thread(target=startCherry)
    t.daemon = True
    t.start()
    rospy.init_node('rest_to_topic', anonymous=False)
    rospy.spin()