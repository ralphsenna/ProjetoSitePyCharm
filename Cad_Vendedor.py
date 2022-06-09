import cherrypy
import os
import sqlite3


localDir = os.path.dirname(__file__)


class cadVendedor:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "\Visual\Cadastro_vendedores.html")
        return html

    @cherrypy.expose
    def adTabela (self, nome, email, senha, senha2, cpf):
        if (senha == senha2):
            con = sqlite3.connect("Vendedores.db")
            cursor = con.cursor()
            sql = "insert into vendedores (nome , email, senha, cpf) values ('%s','%s','%s','%s')" % (
            nome, email, senha, cpf)
            cursor.execute(sql)
            con.commit()
            cursor.close()
            con.close()
            html = open(localDir + "\Visual\Login_page.html")
            return html
        else:
            html = open(localDir + "\Visual\Cadastro_vendedores.html")
            return html