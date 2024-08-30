from Calculadora_Model import Model
from Calculadora_View import View

class Controller():
    __model = None
    __view = None

    # Questão 26: (Criar o construtor da classe Controller)
    def __init__(self):
        self.start()

    def start(self):
        # Questão 27: (Alocar os objetos model e view)
        self.__model = Model()
        self.__view = View(self, "Minha Calculadora")

    def action_Adicionar(self):
        # Questão 28: (Criar o evento que calcula a adição dos valores numéricos)
        #             (É obrigatório usar tratamento de exceções)
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.adiciona_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

    def action_Subtrair(self):
        # Questão 29: (Criar o evento que calcula a subtração dos valores numéricos)
        #             (É obrigatório usar tratamento de exceções)
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.subtrai_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

    def action_Multiplicar(self):
        # Questão 30: (Criar o evento que calcula a multiplicação dos valores numéricos)
        #             (É obrigatório usar tratamento de exceções)
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.multiplica_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

    def action_Dividir(self):
        # Questão 31: (Criar o evento que calcula a divisão dos valores numéricos)
        #             (É obrigatório usar tratamento de exceções)
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.divide_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except ZeroDivisionError as zde:
            Erro = "Erro: Divisao por zero: %s" % zde
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)
