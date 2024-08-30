import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class View(QWidget): # (Complete o código que declara a classe View)
    __Lb_valor1 = None
    __Lb_valor2 = None
    __Lb_result = None
    __LEd_valor1 = None
    __LEd_valor2 = None
    __LEd_result = None
    __Bt_adic = None
    __Bt_sub = None
    __Bt_mult = None
    __Bt_div = None
    __Cntr = None

    # Questão 10: (Criar o construtor da classe View)
    def __init__(self, Cntr, Str="Janela"):
        super().__init__()
        self.__Cntr=Cntr
        self.setWindowTitle(Str)
        self.setGeometry(320, 160, 10, 10)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('orange'))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        # Questão 11: (Qual o código necessário para encerrar o programa no canto
        #              superior direito da janela)
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    # Questão 12: (Criar o método get_Valor1)
    def get_Valor1(self):
        return(self.__LEd_valor1.text())

    # Questão 13: (Criar o método get_Valor2)
    def get_Valor2(self):
        return(self.__LEd_valor2.text())

    # Questão 14: (Criar o método set_Resultado)
    def set_Resultado(self, resultado):
        self.__LEd_result.setText("%5.2f" % resultado)

    def action_Bt_adic(self):
        # Questão 15: (Criar o evento que calcula a adição dos valores numéricos)
        self.__Cntr.action_Adicionar()

    def action_Bt_sub(self):
        # Questão 16: (Criar o evento que calcula a subtração dos valores numéricos)
        self.__Cntr.action_Subtrair()

    def action_Bt_mult(self):
        # Questão 17: (Criar o evento que calcula a multiplicação dos valores numéricos)
        self.__Cntr.action_Multiplicar()

    def action_Bt_div(self):
        # Questão 18: (Criar o evento que calcula a divisão dos valores numéricos)
        self.__Cntr.action_Dividir()

    def show_error(self, Erro):
        # Questão 19: (Criar o métodp que mostra uma mensagem de erro na tela com QMessageBox)
        QMessageBox.critical(self, "Janela de Erro", Erro)

    def inicialize(self):
        Grid=QGridLayout()

        # Questão 20: (Realize a alocação dos componentes gráficos)
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        self.__Lb_valor1=QLabel(self, text="Valor1:", width=12)
        self.__Lb_valor2=QLabel(self, text="Valor2:", width=12)
        self.__Lb_result = QLabel(self, text="Resultado:", width=12)

        self.__Lb_valor1.setAlignment(Qt.AlignRight)
        self.__Lb_valor2.setAlignment(Qt.AlignRight)
        self.__Lb_result.setAlignment(Qt.AlignRight)

        self.__Lb_valor1.setContentsMargins(4, 4, 4, 4)
        self.__Lb_valor2.setContentsMargins(4, 4, 4, 4)
        self.__Lb_result.setContentsMargins(4, 4, 4, 4)

        self.__Lb_valor1.setAutoFillBackground(True)
        self.__Lb_valor1.setPalette(p1)

        self.__Lb_valor2.setAutoFillBackground(True)
        self.__Lb_valor2.setPalette(p1)

        self.__Lb_result.setAutoFillBackground(True)
        self.__Lb_result.setPalette(p1)

        self.__LEd_valor1=QLineEdit(self, width=28)
        self.__LEd_valor2=QLineEdit(self, width=28)
        self.__LEd_result=QLineEdit(self, width=28)

        self.__Bt_adic=QPushButton(self, text='Adicionar')
        # Questão 21: (Conectar o botão Bt_adic ao evento que realiza a adição dos valores numéricos)
        self.__Bt_adic.clicked.connect(self.action_Bt_adic)

        self.__Bt_sub = QPushButton(self, text='Subtrair')
        # Questão 22: (Conectar o botão Bt_sub ao evento que realiza a subtração dos valores numéricos)
        self.__Bt_sub.clicked.connect(self.action_Bt_sub)

        self.__Bt_mult = QPushButton(self, text='Multiplicar')
        # Questão 23: (Conectar o botão Bt_mult ao evento que realiza a multiplicação dos valores numéricos)
        self.__Bt_mult.clicked.connect(self.action_Bt_mult)

        self.__Bt_div = QPushButton(self, text='Dividir')
        # Questão 24: (Conectar o botão Bt_div ao evento que realiza a divisão dos valores numéricos)
        self.__Bt_div.clicked.connect(self.action_Bt_div)

        # Questão 25: (Acrescentar os componentes gráficos na Tela)
        Grid.addWidget(self.__Lb_valor1, 0, 0)
        Grid.addWidget(self.__Lb_valor2, 1, 0)

        Grid.addWidget(self.__LEd_valor1, 0, 1, 1, 4)
        Grid.addWidget(self.__LEd_valor2, 1, 1, 1, 4)

        Grid.addWidget(self.__Bt_adic, 2, 1)
        Grid.addWidget(self.__Bt_sub, 2, 2)
        Grid.addWidget(self.__Bt_mult, 2, 3)
        Grid.addWidget(self.__Bt_div, 2, 4)

        Grid.addWidget(self.__Lb_result, 3, 0)
        Grid.addWidget(self.__LEd_result, 3, 1, 1, 4)

        self.setLayout(Grid)
        self.show()
