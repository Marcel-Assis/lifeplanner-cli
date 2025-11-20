# arquivo storage.py
import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arq:
            # ler o conteúdo do arquivo e retirar os espaços em branco desnecessários se tiver
            conteudo = arq.read().strip()
            # converter o conteúdo JSON de volta para uma lista de tarefas
            return json.loads(conteudo)
    except FileNotFoundError:
        # arquivo não existe, retorna lista vazia
        return []
    except json.JSONDecodeError:
        # arquivo existe mas está corrompido
        print("Arquivo corrompido. Criando novo arquivo de tarefas...")
        return []

    

def salvar_tarefas(tarefas):
    try:
        # salvar a lista de tarefas no arquivo JSON
        with open('tarefas.json', 'w', encoding='utf-8') as arq:
            # converter a lista de tarefas para JSON e escrever no arquivo
            json.dump(tarefas, arq, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")
    
