import cherrypy
import os
import sqlite3


localDir = os.path.dirname(__file__)


class Login:
    email=""
    @cherrypy.expose
    def index(self):
        html = open(localDir + "\Visual\Login_page.html")
        return html

    @cherrypy.expose
    def verificar (self, email, senha):
        con = sqlite3.connect("Vendedores.db")
        cursor = con.cursor()
        sql = ("select email, senha from vendedores where email= '%s' AND senha='%s'" % (email, senha))
        cursor.execute(sql)
        dado = cursor.fetchall()
        cursor.close()
        con.close()
        if dado!=[]:
            self.email=email
            html = open(localDir + "\Visual\Perfil_Cad.html")
            return html
        else:
            html = open(localDir + "\Visual\Login_page.html")
            return html

    @cherrypy.expose
    def excluir (self):
        con = sqlite3.connect("Vendedores.db")
        cursor = con.cursor()
        cursor.execute("delete from vendedores where email= '%s'" % self.email)
        con.commit()
        cursor.close()
        con.close()
        raise cherrypy.HTTPRedirect('/.')

    @cherrypy.expose
    def excluirProduto(self, nome):
        con = sqlite3.connect("Produtos.db")
        cursor = con.cursor()
        cursor.execute("delete from produtos where nome= '%s'" % nome)
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html

    @cherrypy.expose
    def menuAlteracao (self):
        html = open(localDir + "\Visual\MenuAltercao.html")
        return html

    @cherrypy.expose
    def Alterar(self, senha):
        con = sqlite3.connect("Vendedores.db")
        cursor = con.cursor()
        cursor.execute("update vendedores set senha = '%s' where email= '%s'" % (senha, self.email))
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html

    @cherrypy.expose
    def AlterarN(self, nome):
        con = sqlite3.connect("Vendedores.db")
        cursor = con.cursor()
        cursor.execute("update vendedores set nome = '%s' where email= '%s'" % (nome, self.email))
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html

    @cherrypy.expose
    def AlterarE(self, email2):
        con = sqlite3.connect("Vendedores.db")
        cursor = con.cursor()
        cursor.execute("update vendedores set email = '%s' where email= '%s'" % (email2, self.email))
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html

    @cherrypy.expose
    def menuAlteracaoProduto(self):
        html = open(localDir + "\Visual\MenuAltercao_Produto.html")
        return html
    @cherrypy.expose
    def AlterarProdutoP(self, nome, preco):
        con = sqlite3.connect("Produtos.db")
        cursor = con.cursor()
        cursor.execute("update produtos set preco = '%s'  where nome = '%s'" % (preco , nome))
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html

    @cherrypy.expose
    def AlterarProdutoD(self, nome, descricao):
        con = sqlite3.connect("Produtos.db")
        cursor = con.cursor()
        cursor.execute("update produtos set descricao = '%s' where nome = '%s'" % (descricao, nome))
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html

    @cherrypy.expose
    def AlterarProdutoN(self, nome, nome2):
        con = sqlite3.connect("Produtos.db")
        cursor = con.cursor()
        cursor.execute("update produtos set nome = '%s' where nome = '%s'" % (nome2, nome))
        con.commit()
        cursor.close()
        con.close()
        html = open(localDir + "\Visual\Perfil_Cad.html")
        return html