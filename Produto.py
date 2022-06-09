import cherrypy
import os



localDir = os.path.dirname(__file__)


class produto:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "\Visual\Produto.html")
        return html
