import cherrypy
import os
import sqlite3


localDir = os.path.dirname(__file__)


class cadProduto:
    @cherrypy.expose
    def index(self):
        html = open(localDir + "\Visual\Cadastro_Produto.html")
        return html
    @cherrypy.expose
    def adTabela (self, nome, preco, formas, descricao):
        con = sqlite3.connect("Produtos.db")
        cursor = con.cursor()
        sql = "insert into produtos (nome , descricao, pagamento, preco) values ('%s','%s','%s','%s')" % (nome, descricao, formas, preco)
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html
