import cherrypy
import os, os.path

class Server(object):
    @cherrypy.expose
    def status(self):
        return "Ok"

    @cherrypy.expose
    def startLeft(self):
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

if __name__ == '__main__':
    cherrypy.config.update(
        {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 30123,
        })

    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.abspath(os.getcwd()) + '/frontend-app/dist/frontend-app',
            'tools.staticdir.index': 'index.html',
        }
    }

    cherrypy.quickstart(Server(),'/', conf)