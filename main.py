from turingmachine import MaquinaTuring
import os
import sys

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

def main():
    opt = 0
    cadeia = ""

    # ----------------------------------------------------------
    inicial = "init"
    func_trans = {("init","0"):("init", "1", ">"),
                       ("init","1"):("init", "0", ">"),
                       ("init"," "):("final"," ", "*"),
                       }
    finais = {"final"}
    alfa = ["0", "1"]
    desc = "Maquina para inverter binario"
    mt1 = MaquinaTuring(desc, alfa, func_trans, inicial, finais)
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
    alfa = ["a", "b"]
    desc = "Maquina reconhecedora da linguagem L = {a^n b a^n}"
    mt2 = MaquinaTuring(desc, alfa, func_trans, inicial, finais)
    # ----------------------------------------------------------

    while opt > 3 or opt < 1:
        os.system(CLEAR)
        print("--------------OPCOES--------------")
        print("----------------------------------")
        print("1. MT para Inverter Binario")
        print("2. MT para verificar se uma\n   cadeia pertence a\n   L = {w | w = a^n b a^n}")
        print("3. Sair do Programa")
        opt = int(input("Escolha uma opção: "))

    if opt == 3: return
    else:
        cadeia = input("Digite a cadeia: ")
        if cadeia[-1] != " ": cadeia += " "
            
        if opt == 1:
            mt1.processaCadeia(cadeia)
            main()
        else:
            mt2.processaCadeia(cadeia)
            main()



if __name__ == "__main__":
    main()

