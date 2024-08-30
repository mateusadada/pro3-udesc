class Model():
    __valor1=None
    __valor2=None
    __resultado=None

    # Questão 01: (Criar o construtor da classe Model)
    def __init__(self):
        self.__valor1=0
        self.__valor2=0.0
        self.adiciona_valores()

    # Questão 02: (Criar o método set_Valor1)
    def set_Valor1(self, val1):
        self.__valor1=val1

    # Questão 03: (Criar o método set_Valor2)
    def set_Valor2(self, val2):
        self.__valor2=val2

    # Questão 04: (Criar o método get_Resultado)
    def get_Resultado(self):
        return(self.__resultado)

    def adiciona_valores(self):
        # Questão 05: (Completar o código para adicionar os valores)
        self.__resultado=(self.__valor1 + self.__valor2)

    def subtrai_valores(self):
        # Questão 06: (Completar o código para subtrair os valores)
        self.__resultado=(self.__valor1 - self.__valor2)

    def multiplica_valores(self):
        # Questão 07: (Completar o código para multiplicar os valores)
        self.__resultado=(self.__valor1 * self.__valor2)

    def divide_valores(self):
        # Questão 08: (Completar o código para dividir os valores)
        self.__resultado=(self.__valor1 / self.__valor2)
