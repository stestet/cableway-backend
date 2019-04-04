import cherrypy
from subprocess import call
import threading


class CablewayServer(object):
    def __init__(self, motorController):
        self.motor = motorController
        self.timer = None

    @cherrypy.expose
    def status(self):
        return "Ok"

    @cherrypy.expose
    def startLeft(self):
        self.startTimer()      
        self.motor.turnLeft()

    @cherrypy.expose
    def startRight(self):
        self.startTimer()    
        self.motor.turnRight()      

    @cherrypy.expose
    def stop(self):
        print('Stop called')
        if (self.timer != None):
            if (self.timer.is_alive() == True):
                self.timer.cancel()
            self.timer = None
        
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

    
    def startTimer(self):
        if (self.timer == None):
            self.timer = threading.Timer(5.0, self.stop)
            self.timer.start()
        else:
            if (self.timer.is_alive() == False):
                self.timer.start()
