import sys
from PyQt5.QtWidgets import *
from Calculadora_Controller import Controller

# Questão 32: (Aloque um objeto da classe Controller para iniciar o programa)
if __name__ == "__main__":
    App=QApplication(sys.argv)
    Cntr=Controller()
    App.exec_()
