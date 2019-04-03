import cherrypy
from subprocess import call


class CablewayServer(object):
    def __init__(self, motorController):
        self.motor = motorController

    @cherrypy.expose
    def status(self):
        return "Ok"

    @cherrypy.expose
    def startLeft(self):
        self.motor.turnLeft()

    @cherrypy.expose
    def startRight(self):
        self.motor.turnRight()      

    @cherrypy.expose
    def stop(self):
        self.motor.stop()

    @cherrypy.expose
    def faster(self):
        self.motor.faster()

    @cherrypy.expose
    def slower(self):
        self.motor.slower()

    @cherrypy.expose
    def shutdown(self):
        call("sudo shutdown -h now", shell=True)    