from turingmachine import MaquinaTuring
import os
import sys
import pickle

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

def main():
    opt = 0
    cadeia = ""

    # Carrega as maquinas de turing
    dicio_mt = {}
    diretorio = "maquinas_bin"
    for arquivo in os.listdir(diretorio):
        nome = arquivo[:-4]
    
        path = os.path.join(diretorio, arquivo)
        with open(path, 'rb') as mt_arq:
            maquina = pickle.load(mt_arq)
            dicio_mt.update({nome:maquina})

    # Menu com usuario
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
            dicio_mt['invertebin'].processaCadeia(cadeia)
            main()
        else:
            dicio_mt['anban'].processaCadeia(cadeia)
            main()



if __name__ == "__main__":
    main()

