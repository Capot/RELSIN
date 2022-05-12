from PyQt5 import uic, QtWidgets
import consulta as cons


class controlejanela():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.formulario = uic.loadUi("D:\Projetos\Relsin\janelas\janela.ui")
        self.formulario.btn_consultar.clicked.connect(self.consultaJanela)

    def consultaJanela(self):
        empresa = self.formulario.txt_empresa.text()
        print(empresa)
        rel = cons.relatorio()
        rel.con_sql(empresa)
        #rel.imprimeTerminal()
        rel.imprimi()
        # rel.closeconect()

    def constroetela(self):
        self.formulario.show()
        self.app.exec()


#x = controlejanela()
#x.constroetela()
