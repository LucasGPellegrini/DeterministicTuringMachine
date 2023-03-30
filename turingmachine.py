import os
import sys
from time import sleep

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

# Classe para representar Maquina de Turing
class MaquinaTuring:
    def __init__(self,
                 desc = "Maquina de Turing",
                 cadeia = "", 
                 transicoes = None, 
                 est_inicial = "", 
                 ests_finais = None):
        self.cabeca_leitura = 0
        self.simbolo_vazio = " "
        self.estado_atual = est_inicial
        self.ests_finais = set(ests_finais)
        self.cadeia = dict(enumerate(cadeia))
        self.transicoes = transicoes
        self.aceita = False
        self.fim = False
        self.cadeia_inicial = dict(enumerate(cadeia))
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

    def processaCadeia(self):
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

# TESTE

inicial = "init"
func_trans = {("init","0"):("init", "1", ">"),
                       ("init","1"):("init", "0", ">"),
                       ("init"," "):("final"," ", "*"),
                       }
finais = {"final"}
cadeia = "010011001 " 


desc = "Maquina para inverter binario"
t = MaquinaTuring(desc, cadeia, func_trans, inicial, finais)
t.processaCadeia()


# ----------------------------------------------------------

inicial = "q0"
func_trans = {("q0", "a"):("q1", "#", ">"),
                  ("q0", "b"):("q4", "b", ">"),
                  ("q1", "a"):("q1", "a", ">"),
                  ("q1", "b"):("q1", "b", ">"),
                  ("q1", " "):("q2", " ", "<"),
                  ("q1", "#"):("q2", "#", "<"),
                  ("q2", "a"):("q3", "#", "<"),
                  ("q3", "a"):("q3", "a", "<"),
                  ("q3", "b"):("q3", "b", "<"),
                  ("q3", "#"):("q0", "#", ">"),
                  ("q4", "#"):("qf", "#", "*")
              }

finais = {"qf"}
cadeia = "aaabaaa "
desc = "Maquina reconhecedora da linguagem L = {a^n b a^n}"
t = MaquinaTuring(desc, cadeia, func_trans, inicial, finais)
t.processaCadeia()
if t.aceita:
    print("Cadeia aceita!")
else:
    print("Cadeia Rejeitada!")

cadeia = "aaaaabaaaa "
t = MaquinaTuring(desc, cadeia, func_trans, inicial, finais)
t.processaCadeia()
if t.aceita:
    print("Cadeia aceita!")
else:
    print("Cadeia Rejeitada!")

cadeia = "aaabaaaa "
t = MaquinaTuring(desc, cadeia, func_trans, inicial, finais)
t.processaCadeia()
if t.aceita:
    print("Cadeia aceita!")
else:
    print("Cadeia Rejeitada!")
