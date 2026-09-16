def exportar_csv(linhas, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            arquivo.write(",".join(str(v) for v in linha) + "\n")
