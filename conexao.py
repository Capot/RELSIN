import fdb
import PySimpleGUI as sg


class conexao():

    def __init__(self):
        self.host = 'localhost'
        self.database = 'c:\RELSIN\SAIDA.FDB'
        self.user = 'sysdba'
        self.password = 'masterkey'
        self.port = 3050
        self.charset = 'utf-8'

    def conectar(self):
        try:
            self.con = fdb.connect(host=self.host, database=self.database, user=self.user, password=self.password, port=self.port, charset=self.charset)
            return self.con.cursor()

        except fdb.Error as s:
            sg.popup(s, title='Erro de Conexão', icon='SASCC.ico')
            sg.popup('Erro de conexão\nContacte o adminstrador do Produto', title='RELSIN', icon='SASCC.ico')