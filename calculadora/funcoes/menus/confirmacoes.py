def confirmacao(msg):
    while True:
        cf = str(input(msg)).lower()
        if cf == "s" and "S":
            return True
        elif cf == "n" and "N":
            return False
        print("opção inválido!")