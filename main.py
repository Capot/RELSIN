# openpyxl
from PyQt5 import uic, QtWidgets
import PySimpleGUI as sg
import os
import controle


def sim():
    sg.popup('Por favor aguarde.\nEsse processo pode levar algum tempo dependendo de sua internet e hardware',
             title='RELSIN', icon='SASCC.ico')
    try:
        # Cria saida de arquivo de banco
        # firebird=r"cd C:\Program Files\Firebird\Firebird_2_5\bin"
        # exe=r"gbak user SYSDBA pas masterkey r -o 'C:\RELSIN\backup.fbk' C:\RELSIN\SAIDA.fdb"
        x = os.system(
            r'C:\"Program Files"\Firebird\Firebird_2_5\bin\gbak -user SYSDBA -pas masterkey -r -o -REP C:\RELSIN\backup.fbk C:\RELSIN\SAIDA.fdb')
        # print(os.getcwd())
        # path = os.path.join(firebird, exe)
        if x != 0:
            sg.popup('Erro ao extrair dados.\nContacte o desenvolvedor.', title='RELSIN', icon='SASCC.ico')
            print('erro')

        else:
            sg.popup('Processo de Extração Concluido', title='RELSIN', icon='SASCC.ico')
            os.system("echo saindo")
            tela.constroetela()

    except (OSError, IOError, os.error, Exception) as e:
        sg.popup('Erro de conexão\nContacte o adminstrador do Produto', title='RELSIN', icon='SASCC.ico')
        print(e)


def nao():
    tela.constroetela()


if __name__ == "__main__":
    # Instancia Telas, necessário dessa forma
    tela = controle.controlejanela()

    # Inicia tela de entrada
    app = QtWidgets.QApplication([])
    abertura = uic.loadUi(r"D:\Projetos\Relsin\janelas\abertura.ui")

    abertura.btn_sim.clicked.connect(sim)
    abertura.btn_nao.clicked.connect(nao)
    abertura.show()
    app.exec()
    # sys.exit(app1.exec_())
