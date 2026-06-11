# Sistema Escolar em Python

## Descrição

Este projeto consiste em um sistema escolar simples desenvolvido em Python com o objetivo de aplicar conceitos fundamentais de programação, como estruturas condicionais, laços de repetição, dicionários e manipulação de entrada e saída de dados.

O sistema permite que professores ou administradores realizem operações básicas de gerenciamento escolar, incluindo cadastro de alunos, consulta de matrículas, lançamento de notas e consulta de boletins.

---

## Funcionalidades

### Autenticação de Usuário

Antes de acessar o sistema, o usuário deve informar suas credenciais de acesso.

Credenciais padrão:

```python
Usuário: admin
Senha: 123
```

### Cadastro de Alunos

Permite cadastrar novos alunos informando:

* Nome do aluno
* Número da matrícula

As informações são armazenadas em um dicionário.

### Consulta de Alunos

Permite consultar alunos cadastrados por meio do nome e visualizar suas respectivas matrículas.

### Lançamento de Notas

Permite registrar ou atualizar a média de um aluno.

As notas são armazenadas em um dicionário específico para esse fim.

### Consulta de Boletim

Permite consultar a média registrada de um aluno a partir do seu nome.

### Encerramento do Sistema

Permite finalizar a execução do programa de forma controlada.

---
## Estrutura de Dados

### Dicionário de Matrículas

```python
matricula = {
    "Eduardo": 1,
    "Lucas": 2
}
```

### Dicionário de Notas

```python
notas = {
    "Eduardo": 9.5,
    "Lucas": 10
}
```


## Menu Principal

```text
1 - Cadastrar Aluno
2 - Listar Alunos
3 - Lançar Notas
4 - Consultar Boletim
5 - Sair
```
