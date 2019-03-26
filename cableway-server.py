import cherrypy


class CablewayController(object):
    @cherrypy.expose
    def index(self):
        return "Ready to serve!"


if __name__ == '__main__':
    cherrypy.quickstart(CablewayController())