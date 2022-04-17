from cytolk import  tolk

def carregar():
    return tolk.load()

def detectar():
    if tolk.detect_screen_reader():
        return True
    else:
        return False

def falar():
    if tolk.has_speech():
        return True
    else:
        return False

