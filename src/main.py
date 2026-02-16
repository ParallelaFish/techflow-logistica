# src/main.py

class SistemaLogistica:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        if not descricao:
            return "Erro: Descrição vazia"
        tarefa = {"id": len(self.tarefas) + 1, "descricao": descricao, "status": "A Fazer"}
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return self.tarefas
