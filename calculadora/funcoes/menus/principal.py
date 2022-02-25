from  funcoes.menus import iniciar
from funcoes.menus import  resultados
from  funcoes.menus import limpar

def menu():
    print("Menu principal")
    while True:
        opcoes = str(input(
            "Calculadora qual a opção que deseja: \+"
            "\ni Iniciar calculadora: "
            "\nv Ver histórico de resultados: "
            "\nl Limpar histórico: "
            "\ns Sair: "
        )).lower()
        if opcoes == "i" and "I":
            iniciar.iniciar()
        if opcoes == "v" and "V":
            resultados.verHistorico()
        if opcoes == "l" and "L":
            limpar.limparMemoria()