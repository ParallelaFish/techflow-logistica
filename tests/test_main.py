# tests/test_main.py
from src.main import SistemaLogistica

def test_adicionar_tarefa_sucesso():
    sistema = SistemaLogistica()
    resultado = sistema.adicionar_tarefa("Entrega Rota A")
    assert resultado["descricao"] == "Entrega Rota A"
    assert len(sistema.listar_tarefas()) == 1

def test_adicionar_tarefa_vazia():
    sistema = SistemaLogistica()
    resultado = sistema.adicionar_tarefa("")
    assert resultado == "Erro: Descrição vazia"
