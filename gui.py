import functions
import PySimpleGUI as sg
import time

nomeArquivo = "tarefas.txt"

sg.theme("Black")

relogio = sg.Text("", key="relogio")
label = sg.Text("Tarefa:")

inputBox = sg.InputText(tooltip="Digite a tarefa", key="tarefa")

addButton = sg.Button("Adicionar", size=10, mouseover_colors="Green")
editButton = sg.Button("Editar")
deleteButton = sg.Button("Excluir", mouseover_colors="Red")
closeButton = sg.Button("SAIR", pad=((150, 0)), size=10, mouseover_colors="Red")

listBox = sg.Listbox(values=functions.getList(nomeArquivo), key="tarefas", 
                                enable_events=True, size=[45,10])

window = sg.Window('Lista de Tarefas', 
                            layout = [[relogio],
                            [label, inputBox, addButton], 
                            [listBox, sg.Column([[editButton], [deleteButton]])],
                            [closeButton]],
                            #element_justification = "center",
                            font=('Helvetica', 10))

while True:
    comando, tarefa = window.read(timeout=200)
    window["relogio"].update(value=time.strftime("%d %b, %Y %H:%M:%S"))
    #print(comando)
    #print(tarefa)

    match comando:
        case "Adicionar":
            if tarefa['tarefa'] != '':
                if "\n" in tarefa['tarefa']:
                    tarefa['tarefa'] = tarefa['tarefa'][:-1]
                tarefas = functions.getList(nomeArquivo)
                tarefas.append(tarefa['tarefa'] + "\n")
                functions.writeList(nomeArquivo, tarefas)
                window['tarefas'].update(values=tarefas)
        case "Editar":
            try:
                if tarefa['tarefa'] != tarefa['tarefas'][0]:
                    tarefas = functions.getList(nomeArquivo)
                    #index = tarefas.index(tarefa['tarefas'][0])
                    tarefas[tarefas.index(tarefa['tarefas'][0])] = tarefa['tarefa'] + "\n" 
                    functions.writeList(nomeArquivo, tarefas)
                    window['tarefas'].update(values=tarefas)
            except IndexError:
                sg.popup("Selecione um item para editar.",  font=('Helvetica', 10))
        case "Excluir":
            try:
                tarefas = functions.getList(nomeArquivo)
                tarefas.remove(tarefa['tarefas'][0])
                functions.writeList(nomeArquivo, tarefas)
                window['tarefas'].update(values=tarefas)
            except IndexError:
                sg.popup("Selecione um item para excluir.",  font=('Helvetica', 10))
        case "tarefas":
            window['tarefa'].update(value=tarefa['tarefas'][0])
        
        case sg.WIN_CLOSED | "SAIR":
            break

window.close()