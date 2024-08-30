import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class View(QWidget): # (Complete o código que declara a View)
    __Lb_peso = None
    __Lb_altura = None
    __Lb_imc = None
    __Lb_classif = None
    __LEd_peso = None
    __LEd_altura = None
    __LEd_imc = None
    __LEd_classif = None
    __Bt_calc = None
    __Cntr = None

    # Questão 08: (Criar o construtor da classe View)
    def __init__(self,Cntr,Str="Janela"):
        super().__init__()
        self.setWindowTitle(Str)
        self.__Cntr=Cntr
        self.setGeometry(520, 280, 10, 10)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('orange'))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        # Questão 09: (Qual o código necessário para encerrar o programa no canto
        #              superior direito da janela)
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    # Questão 10: (Criar o método get_Peso)
    def get_Peso(self):
        return (self.__LEd_peso.text())

    # Questão 11: (Criar o método get_Altura)
    def get_Altura(self):
        return (self.__LEd_altura.text())

    # Questão 12: (Criar o método set_imc)
    def set_imc(self, imc):
        self.__LEd_imc.setText("%5.2f" % imc)

    # Questão 13: (Criar o método set_classif)
    def set_classif(self,classificacao):
        self.__LEd_classif.setText(classificacao)

    def action_Bt_calc(self):
        # Questão 14: (Criar o evento que calcula o imc e
        #              define a classificação de risco)
        self.__Cntr.action_Calcular()

    def show_error(self, Erro):
        # Questão 15: (Criar o método que mostra uma mensagem de erro na tela com QMessageBox)
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Erro")
        error_box.setText(Erro)
        error_box.exec_()

    def inicialize(self):
        Grid=QGridLayout()

        # Questão 16: (Realize a alocação dos componentes gráficos)
        self.__Lb_peso=QLabel(self, text="Peso:", width=12)
        self.__Lb_altura=QLabel(self, text="Altura:", width=12)
        self.__Lb_imc=QLabel(self, text="IMC:", width=12)
        self.__Lb_classif=QLabel(self, text="Classificação:", width=12)
        
        self.__LEd_peso=QLineEdit(self, width=28)
        self.__LEd_altura=QLineEdit(self, width=28)
        self.__LEd_imc=QLineEdit(self, width=28)
        self.__LEd_classif=QLineEdit(self, width=28)

        self.__Bt_calc=QPushButton(self, text='Calcular')
        # Questão 17: (Conectar o botão Bt_adic ao evento que realiza
        #             o cálculo do imc e define a classificação de risco)
        self.__Bt_calc.clicked.connect(self.action_Bt_calc)

        # Questão 18: (Acrescentar os componentes gráficos na Tela)
        Grid.addWidget(self.__Lb_peso, 0, 0)
        Grid.addWidget(self.__Lb_altura, 1, 0)
        Grid.addWidget(self.__Lb_imc, 3, 0)
        Grid.addWidget(self.__Lb_classif, 4, 0)
        
        Grid.addWidget(self.__LEd_peso, 0, 1, 1, 1)
        Grid.addWidget(self.__LEd_altura, 1, 1, 1, 1)
        Grid.addWidget(self.__LEd_imc, 3, 1, 1, 1)
        Grid.addWidget(self.__LEd_classif, 4, 1, 1, 1)
        
        Grid.addWidget(self.__Bt_calc, 2, 0)

        self.setLayout(Grid)
        self.show()
