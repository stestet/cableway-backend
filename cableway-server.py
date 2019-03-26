import cherrypy


class CablewayController(object):
    @cherrypy.expose
    def index(self):
        return "Ready to serve!"


if __name__ == '__main__':
    cherrypy.config.update(
        {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 30123,
        })
    cherrypy.quickstart(CablewayController())