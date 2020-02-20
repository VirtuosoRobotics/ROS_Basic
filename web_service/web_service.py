#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy,os,time
import subprocess,signal
import threading

cwd = os.getcwd()

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    },
    '/': {
        'tools.sessions.on': True,
        'tools.staticdir.root': '%s' %cwd,
    },
    '/web/css': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'web/css',
    }
}

class RobotWeb(object):

    def __init__(self):
        self.ros_master = '192.168.30.5'
        return

    @cherrypy.expose
    def index(self):
        return open('./web/home.html')

    @cherrypy.expose
    def pub_once_input(self):
        return open('./web/pub_once.html')
    
    @cherrypy.expose
    def pub_repeatly_input(self):
        return open('./web/pub_repeatly.html')

    @cherrypy.expose
    def pub_once(self,topic_name,message_type,message):
        subprocess.Popen(['bash ./bash_script/pub_once.bash '+self.ros_master+' '+topic_name +' '+message_type +' ' +message], shell=True)
        return 'OK'

    @cherrypy.expose
    def pub_repeatly(self,topic_name,message_type,message,frequency):
        subprocess.Popen(['bash ./bash_script/pub_repeatly.bash '+self.ros_master+' '+topic_name +' '+message_type +' ' +message +' '+frequency], shell=True)
        return open('./web/stop_pub.html')

    @cherrypy.expose
    def stop_publish(self):
        os.system("ps aux | grep pub | awk '{print $2}' | xargs kill -9")
        return 'stop publish'

if __name__ == "__main__":
    cherrypy.quickstart(RobotWeb(), '/',config)
