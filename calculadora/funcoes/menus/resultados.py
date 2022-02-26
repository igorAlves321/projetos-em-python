from  funcoes.menus import iniciar

def verHistorico():
    mostrar = iniciar.historico
    for c in mostrar:
        print(f"Resultados na memória: {mostrar}")
        break
    else:
        print("Nada para mostrar no histórico!")