import streamlit as st
import functions

nomeArquivo = "tarefas.txt"
tarefas = functions.getList(nomeArquivo)

def addTarefa():
    tarefa = st.session_state["novaTarefa"] + "\n"
    tarefas.append(tarefa) 
    functions.writeList(nomeArquivo, tarefas)

st.title("Lista de Tarefas")
st.subheader("Selecione uma tarefa para remover da lista")

st.text_input(label="", placeholder="Nova tarefa...",
              on_change=addTarefa, key="novaTarefa")

for i, tarefa in enumerate(tarefas):
    try:
        selecionado = st.checkbox(tarefa, key=tarefa)
    except st.errors.DuplicateWidgetID:
        tarefas.pop(i)
        functions.writeList(nomeArquivo, tarefas)
        print("Ja existe")
    if(selecionado):
        tarefas.pop(i)
        functions.writeList(nomeArquivo, tarefas)
        del st.session_state[tarefa]
        st.experimental_rerun()

#st.session_state
#st.session_state["novaTarefa"] 