# Simulador de Dados
# Objetivo: Simular o uso de um dado, gerando um valor de 1 até 6

# Importação das Bibliotecas
import random
import PySimpleGUI as sg

# Criação da Classe
class SimuladorDeDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

        # Criação de layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]        
        ]
    
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Manipulação de valores
        try:
            if self.eventos == 'sim' or self.eventos =='s':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')
        except Exception as e:
            print('Ocorreu um erro ao imprimir sua resposta...')
            print('Erro: ', e) 

    def GerarValorDoDado(self):
        print(random.randint(self.valor_min, self.valor_max))

simulador = SimuladorDeDado()
simulador.Iniciar()

