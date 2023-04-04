import os
import sys
from time import sleep

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

# Classe para representar Maquina de Turing
class MaquinaTuring:
    def __init__(self,
                 desc = "Maquina de Turing",
                 alfabeto = "", 
                 transicoes = None, 
                 est_inicial = "", 
                 ests_finais = None):
        self.cabeca_leitura = 0
        self.simbolo_vazio = " "
        self.estado_atual = est_inicial
        self.ests_finais = set(ests_finais)
        self.transicoes = transicoes
        self.alfabeto = alfabeto
        self.aceita = False
        self.fim = False
        self.cadeia_inicial = ""
        self.cadeia = ""
        self.descricao = desc

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
        # Cadeia Inicial
        os.system('clear')
        self.printa()
        print(f"Cabeca de Leitura => ^")
        print(f"Estado Atual      => {self.estado_atual}")
        sleep(1)
        os.system(CLEAR)

        # Processamento
        while not self.fim:
            self.processa()
            # Impressao
            cabeca_pos = " " * self.cabeca_leitura
            cabeca_pos += "^"
            self.printa()
            print(f"Cabeca de Leitura => {cabeca_pos}")
            print(f"Estado Atual      => {self.estado_atual}")
            sleep(1)
            os.system(CLEAR)

        self.printa()
        print("*****************")
        print("  Cadeia Aceita !") if self.aceita else "Cadeia Rejeitada!"
        print("*****************")
        sleep(2)

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

