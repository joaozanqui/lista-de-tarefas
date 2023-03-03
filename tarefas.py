# from functions import getList, writeList
import functions
import time

nomeArquivo = "tarefas.txt"

print(time.strftime("\n%b %d, %Y. %H:%M:%S\n"))

while True:
    try:
        opc = int(input("\n1 - Adicionar\n2 - Ver tarefas\n3 - Remover tarefa\n4 - Editar tarefa\n0 - SAIR\n\t-> "))
        match opc:
            case 1:
                tarefa = input("Nova tarefa ('0' para voltar): ")

                if tarefa != "0":
                    tarefas = functions.getList(nomeArquivo)
                    tarefas.append(tarefa + "\n")
                    functions.writeList(nomeArquivo, tarefas)

            case 2:
                tarefas = functions.getList(nomeArquivo)

                if len(tarefas) <= 0:
                    print("\nNão existem tarefas na lista...")

                else:
                    print("\nTarefas:")
                    for i, tarefa in enumerate(tarefas):
                        tarefa = tarefa.strip('\n')
                        print(f"\t{i+1} - {tarefa}")

            case 3:
                tarefas = functions.getList(nomeArquivo)
                
                remover = int(input("\nÍndice da tarefa ('0' para voltar): "))
                if remover > 0 and remover <= len(tarefas):
                    remover = remover - 1
                    removido = tarefas[remover].strip('\n')

                    novaTarefas = []
                    for i, tarefa in enumerate(tarefas):
                        if i != remover:
                            novaTarefas.append(tarefa)
                    functions.writeList(nomeArquivo, novaTarefas)
                    print(f"'{removido}' removido com sucesso...")

                elif remover > len(tarefas):
                    print(f"\nNão exite tarefas com índice {remover}...")

            case 4:
                tarefas = functions.getList(nomeArquivo)

                editar = int(input("\nÍndice da tarefa ('0' para voltar): "))
                if editar > 0 and editar <= len(tarefas):
                    editar = editar - 1

                    editado = tarefas[editar].strip('\n')
                    
                    novaTarefa = input("Nova tarefa: ")
                    tarefas[editar] = novaTarefa + "\n"

                    novaTarefas = []
                    for i, tarefa in enumerate(tarefas):
                        novaTarefas.append(tarefa)
                    
                    functions.writeList(nomeArquivo, novaTarefas)

                    print(f"'{editado}' editado para '{novaTarefa}' com sucesso...")
                elif editar > len(tarefas):
                    print(f"\nNão exite tarefa com índice {editar}...")
            case 0:
                break

            case _:
                print("\nEscolha uma opção válida...")
    except ValueError:
        print("\nValor inválido...")