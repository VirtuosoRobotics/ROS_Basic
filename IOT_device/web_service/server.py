#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import threading
import time
import serial

nanoSerial = serial.Serial("/dev/ttyUSB0", 9600)
sonic_value = ''

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)
        
    @cherrypy.expose
    def sonic(self):
        return sonic_value

def startCherry():
    cherrypy.quickstart(HelloWorld())

t = threading.Thread(target=startCherry)
t.daemon = True
t.start()

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

