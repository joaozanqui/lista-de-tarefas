def getList(nomeArquivo):
    with open(nomeArquivo, "r") as file:
        tarefas = file.readlines()
    return tarefas


def writeList(nomeArquivo, tarefas):
    with open("tarefas.txt", "w") as file:
        file.writelines(tarefas)
