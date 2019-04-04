import cherrypy
import os, os.path
import motorcontroller as mc
import cablewayserver as server

if __name__ == '__main__':
    cherrypy.config.update(
        {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 30123,
        })

    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.dirname(os.path.abspath(__file__)) + '/frontend-app/dist/frontend-app',
            'tools.staticdir.index': 'index.html',
        }
    }
    
    motorcontroller = mc.MotorController()
    cherrypy.quickstart(server.CablewayServer(motorcontroller),'/', conf)