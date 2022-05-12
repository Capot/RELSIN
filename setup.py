# comando python ./setup build
import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os", "tkinter", "pandas", "PyQt5", "fdb", 'lxml.etree', 'PySimpleGUI'],
                     "includes": ["conexao", "consulta", "controle"],
                     "include_files": [
                         r'D:\Projetos\Relsin\janelas\abertura.ui',
                         r'D:\Projetos\Relsin\janelas\janela.ui']
                     }

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="RELSIN",
    version="0.1",
    description="Relatório Específicos",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon='SASCC.ico', target_name='RELSIN.exe')]
)

# setup(
#     name="RELSIN",
#     version="0.1",
#     description="Relatório Específicos",
#     options=dict(build_exe=build_exe_options),
#     executables=[Executable("main.py", base=base)]
# )