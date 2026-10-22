=======
# Lista de Tarefas

Um programa de lista de tarefas feito em Python com CustomTkinter. Fiz esse projeto mais para aprender a mexer com a biblioteca do que pelo programa em si. É também o meu primeiro repositório no GitHub, então vou ir atualizando este README conforme o projeto andar.

## O que ele vai fazer

- [x] Adicionar tarefas (abre uma janela com título, detalhes e um preview)
- [ ] Mostrar as tarefas em uma lista de blocos
- [ ] Caixa de seleção em cada tarefa
- [ ] Contador no topo, tipo "1 de 3 tarefas concluídas"
- [ ] Botão X para apagar a tarefa
- [ ] Salvar tudo em um arquivo .json automaticamente

## O que quero tentar depois

- Editar uma tarefa que já existe
- Riscar o título quando a tarefa for concluída
- Pedir confirmação antes de apagar
- Filtros (todas, pendentes, concluídas) e busca por título
- Data limite e prioridade
- Uma janela de configurações

## Como rodar

Você precisa ter o [uv](https://docs.astral.sh/uv/) instalado. Ele cuida do Python e das dependências.

1. Baixe o projeto:

```
git clone https://github.com/NotJeej/lista-de-tarefas.git
cd lista-de-tarefas
```

2. Instale as dependências (o uv lê o `pyproject.toml` e instala o CustomTkinter):

```
uv sync
```

3. Rode o programa:

```
uv run python main.py
```

Troque `main.py` pelo nome do arquivo principal do projeto.

## Andamento

Por enquanto só a janela de nova tarefa está pronta. O resto estou fazendo aos poucos.
