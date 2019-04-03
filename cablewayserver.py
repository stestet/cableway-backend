import cherrypy
import os, os.path
import motorcontroller as mc

class CablewayServer(object):
    def __init__(self, motorController):
        self.motor = motorController

    @cherrypy.expose
    def status(self):
        return "Ok"

    @cherrypy.expose
    def startLeft(self):
        self.motor.turnLeft()
        return "turning left"

    @cherrypy.expose
    def startRight(self):
        return "turning right"       

    @cherrypy.expose
    def stop(self):
        return "stop"  

    @cherrypy.expose
    def faster(self):
        return "faster" 

    @cherrypy.expose
    def slower(self):
        return "slower"