from datetime import datetime


def registrar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as arquivo:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"[{data}] {mensagem}\n")