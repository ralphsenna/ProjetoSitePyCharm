import cherrypy
import os

from Cad_Vendedor import cadVendedor
from Cad_produto import cadProduto
from LOGIN import Login
from Produto import produto

localDir = os.path.dirname(__file__)


class Principal:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "\Visual\Main_page.html")
        return html

principal = Principal()
principal.login = Login()
principal.cad_produto = cadProduto()
principal.cad_vendedores = cadVendedor()
principal.produto = produto()

local_config={'/':{'tools.staticdir.on':True,
                   'tools.staticdir.dir':localDir},}

cherrypy.quickstart(principal, config=local_config)