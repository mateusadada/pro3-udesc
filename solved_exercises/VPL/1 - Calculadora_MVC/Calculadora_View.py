import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class View(Questão 09):  ## (Complete o código que declara a classe View)
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

    ## Questão 10:  (Criar o construtor da classe View)

    def closeEvent(self, event):
        ## Questão 11:  (Qual o código necessário para encerrar o programa no canto
        ##               superior direito da janela)

    ## Questão 12:  (Criar o método get_Valor1)

    ## Questão 13:  (Criar o método get_Valor2)

    ## Questão 14:  (Criar o método set_Resultado)

    def action_Bt_adic(self):
        ## Questão 15:  (Criar o evento que calcula a adição dos valores numéricos)

    def action_Bt_sub(self):
        ## Questão 16:  (Criar o evento que calcula a subtração dos valores numéricos)

    def action_Bt_mult(self):
        ## Questão 17:  (Criar o evento que calcula a multiplicação dos valores numéricos)

    def action_Bt_div(self):
        ## Questão 18:  (Criar o evento que calcula a divisão dos valores numéricos)

    def show_error(self, Erro):
        ## Questão 19:  (Criar o métodp que mostra uma mensagem de erro na tela com QMessageBox)

    def inicialize(self):
        Grid=QGridLayout()

        ## Questão 20:  (Realize a alocação dos componentes gráficos)

        self.__Bt_adic=QPushButton(self, text='Adicionar')
        ## Questão 21:  (Conectar o botão Bt_adic ao evento que realiza a adição dos valores numéricos)

        self.__Bt_sub = QPushButton(self, text='Subtrair')
        ## Questão 22:  (Conectar o botão Bt_sub ao evento que realiza a subtração dos valores numéricos)

        self.__Bt_mult = QPushButton(self, text='Multiplicar')
        ## Questão 23:  (Conectar o botão Bt_mult ao evento que realiza a multiplicação dos valores numéricos)

        self.__Bt_div = QPushButton(self, text='Dividir')
        ## Questão 24:  (Conectar o botão Bt_div ao evento que realiza a divisão dos valores numéricos)

        ############# Grid #############
        ## Questão 25:  (Acrescentar os componentes gráficos na Tela)

        self.setLayout(Grid)
        self.show()

##################################################
