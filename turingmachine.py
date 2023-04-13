import os
import sys
from time import sleep

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

# Classe para representar Maquina de Turing
class MaquinaTuring:
    def __init__(self,
                 estados = None,
                 alfa_fita = None,
                 vazio = " ",
                 sigma = None,
                 transicoes = None, 
                 est_inicial = "", 
                 ests_finais = None,
                 desc = "Maquina de Turing"):
        # Elementos da Maquina
        self.simbolo_vazio = vazio
        self.estado_atual = est_inicial
        self.ests_finais = set(ests_finais)
        self.transicoes = transicoes
        self.alfabeto = sigma
        self.alfa_fita = alfa_fita
        self.estados = estados
        self.descricao = desc

        # Elementos de classe (funcionamento)
        self.cabeca_leitura = 0
        self.aceita = False
        self.fim = False
        self.cadeia_inicial = ""
        self.cadeia = ""

    def processa(self):
        caractere = self.cadeia[self.cabeca_leitura]
        transicao = (self.estado_atual, caractere)

        if transicao in self.transicoes:
            estado, acao, direcao = self.transicoes[transicao]
            self.cadeia[self.cabeca_leitura] = acao
              
            if direcao == ">":
                self.cabeca_leitura += 1
            elif direcao == "<":
                self.cabeca_leitura -= 1
            # se nao, nao percorre a cadeia (direcao == "*")
                
            self.estado_atual = estado
        else:
            if self.estado_atual in self.ests_finais:
                self.aceita = True
            self.fim = True

    def processaCadeia(self, cadeia):
        self.cadeia_inicial = dict(enumerate(cadeia))
        self.cadeia = dict(enumerate(cadeia))

        if not self.valida_cadeia():
            print("-----ATENCAO-----")
            print(">Cadeia Invalida!")
            sleep(3)
            return

        # Cadeia Inicial
        caractere = self.cadeia[self.cabeca_leitura]
        transicao = (self.estado_atual, caractere)
        os.system('clear')
        self.printa()
        print(f"Cabeca de Leitura => ^")
        print(f"Estado Atual      => {self.estado_atual}")
        print(f"Transicao         => ")
        if transicao in self.transicoes:
            print('\u03B4'+ f"{transicao} = {self.transicoes[transicao]}")
        else: print(f"Nao ha funcao de transicao definida para {transicao}!")
        sleep(2)
        os.system(CLEAR)

        # Processamento
        while not self.fim:
            self.processa()
            caractere = self.cadeia[self.cabeca_leitura]
            transicao = (self.estado_atual, caractere)
            # Impressao
            cabeca_pos = " " * self.cabeca_leitura
            cabeca_pos += "^"
            self.printa()
            print(f"Cabeca de Leitura => {cabeca_pos}")
            print(f"Estado Atual      => {self.estado_atual}")
            print(f"Transicao         => ")
            if transicao in self.transicoes:
                print('\u03B4'+ f"{transicao} = {self.transicoes[transicao]}")
            else: print(f"Nao ha funcao de transicao definida para {transicao}!")
            sleep(2)
            os.system(CLEAR)

        self.printa()
        print("*****************")
        print("  Cadeia Aceita !") if self.aceita else print("Cadeia Rejeitada!")
        print("*****************")
        sleep(3)

    def printa(self):
        print(f"{'=-'*(len(self.descricao)//2)}")
        print(self.descricao)
        print(f"{'=-'*(len(self.descricao)//2)}\n")
        print(f"Cadeia inicial    => {self.cadeia_to_string('ini')}")
        print(f"Cadeia processada => {self.cadeia_to_string()}")

    def cadeia_to_string(self, cadeia=""):
        if cadeia == "ini":
            string = ""
            for caractere in self.cadeia_inicial.values():
                string += str(caractere)
            return string
        else:
            string = ""
            for caractere in self.cadeia.values():
                string += str(caractere)
            return string
    
    def valida_cadeia(self):
        for caractere in self.cadeia.values():
            if (
                str(caractere) not in self.alfabeto and
                str(caractere) != self.simbolo_vazio
            ): 
                return False

        return True
