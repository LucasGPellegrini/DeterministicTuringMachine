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
        try:
            caractere = self.cadeia[self.cabeca_leitura]
        except IndexError:
            self.cadeia[self.cabeca_leitura] = self.simbolo_vazio
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

        # Prepara os dados que serao escritos no arquivo
        conteudo_arqv = self.__setuplaToString()
        passo_a_passo = ""
        
        # Processamento
        while not self.fim:
            os.system(CLEAR)
            caractere = self.cadeia[self.cabeca_leitura]
            transicao = (self.estado_atual, caractere)

            # Impressao
            cabeca_pos = " " * self.cabeca_leitura
            cabeca_pos += "^"
            self.printa()
            print(f"Cabeca de Leitura => {cabeca_pos}")
            print(f"Estado Atual      => {self.estado_atual}")
            print(f"Transicao         => ")
            passo_a_passo += "Cadeia processada => " + self.cadeia_to_string() + "\n"
            passo_a_passo += "Cabeca de Leitura => " + cabeca_pos + "\n"
            passo_a_passo += "Estado Atual      => " + self.estado_atual + "\n"
            if transicao in self.transicoes:
                print('\u03B4'+ f"{transicao} = {self.transicoes[transicao]}")
                passo_a_passo += '\u03B4'+ str(transicao) + " = " + str(self.transicoes[transicao]) + "\n\n"
            else: 
                print(f"Nao ha funcao de transicao definida para {transicao}!")
                passo_a_passo += "Nao ha funcao de transicao definida para "+ str(transicao) + "\n\n"
            self.processa()
            sleep(2)

        conteudo_arqv += "Cadeia processada => " + self.cadeia_to_string()
        self.printa()
        print("*****************")
        if self.aceita:
            print("  Cadeia Aceita !")
            conteudo_arqv += "CADEIA ACEITA!"
        else:
            print("Cadeia Rejeitada!")
            conteudo_arqv += "CADEIA REJEITADA!"
        print("*****************")
        sleep(3)
        conteudo_arqv += "\n\n"

        self.__salva_no_arqv(conteudo_arqv, passo_a_passo)

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

    def verifica_maquina(self):
        for estado, transicao in self.transicoes.items():
            est_atual, simbolo = estado
            est_proxm, si_novo, direcao = transicao

            if (
                str(est_atual) not in self.estados or
                str(est_proxm) not in self.estados or

                str(simbolo) not in self.alfa_fita or
                str(si_novo) not in self.alfa_fita
            ):
                return False

        return True

    def __setuplaToString(self):
        setupla = ""
        setupla += "Estados: " + str(self.estados) + "\n"
        setupla += "Alfabeto da Fita: " + str(self.alfa_fita) + "\n"
        setupla += "Simbolo Vazio: '" + str(self.simbolo_vazio) + "'\n"
        setupla += "Alfabeto (" + '\u03A3' + "): " + str(self.alfabeto) + "\n"
        setupla += "Estado inicial: " + str(self.estado_atual) + "\n"
        setupla += "Estados Finais: " + str(self.ests_finais) + "\n"
        setupla += "Transicoes (" + '\u03B4' + "): " + str(self.transicoes) + "\n"
        setupla += "-----------------------------------------------\n"
        setupla += "Cadeia inicial    => " + str(self.cadeia_to_string('ini')) + "\n"
        
        return setupla

    def __salva_no_arqv(self, cabecalho, passos):
        string = ""
        string += cabecalho
        string += "------------PASSO-A-PASSO------------\n"
        string += passos

        nome = ''
        for char in list(self.cadeia_inicial.values())[:-1]:
            nome += char
        diretorio = "execucoes"
        path = os.path.join(diretorio, nome)
        with open(path, 'w') as arqv:
            arqv.write(string)

