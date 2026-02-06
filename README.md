# Arch-MVC com FastAPI 🔐🚀

Projeto desenvolvido com o objetivo **exclusivo de aprendizagem**, focado na compreensão e aplicação da **arquitetura MVC (Model–View–Controller)** em APIs Python utilizando **FastAPI**.

Além do MVC, o projeto implementa **autenticação via JWT**, **middleware de segurança** e **persistência de dados com PostgreSQL usando SQLAlchemy**.

---

## 🎯 Objetivo do Projeto

- Entender na prática a **arquitetura MVC**
- Separar corretamente responsabilidades entre:
  - Controllers
  - Models
  - Views (camada de apresentação / API)
- Implementar **autenticação moderna com JWT**
- Trabalhar com **FastAPI** de forma organizada
- Conectar a aplicação a um banco **PostgreSQL**
- Aplicar conceitos reais usados em projetos profissionais

📌 **Este projeto não tem fins produtivos**, sendo voltado apenas para estudo e experimentação.

---

## 🧱 Arquitetura Utilizada

O projeto segue o padrão **MVC**, adaptado ao contexto de APIs REST:


ARCH-MVC/
│
├── .vscode/
│
├── src/
│   ├── controllers/           # Regras de negócio
│   │   ├── __init__.py
│   │   ├── login_controller.py
│   │   ├── people_finder_controller.py
│   │   └── people_register_controller.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   │
│   │   ├── connections/       # Conexão com o banco
│   │   │   ├── __init__.py
│   │   │   └── database.py
│   │   │   └── session.py
│   │   │
│   │   ├── entities/          # Entidades do domínio
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   └── person.py
│   │   │
│   │   └── repository/        # Acesso a dados (SQLAlchemy)
│   │       ├── __init__.py
│   │       ├── user_repository.py
│   │       └── person_repository.py
│   │
│   ├── routes/                # Camada de entrada (FastAPI)
│   │   ├── __init__.py
│   │   ├── auth_route.py
│   │   └── people_finder_route.py
│   │   └── people_register_route.py
│   │
│   ├── schemas/               # DTOs / Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── auth_schema.py
│   │   └── person_schema.py
│   │
│   ├── security/              # JWT, OAuth2, dependências
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   ├── dependencies.py
│   │
│   └── __init__.py
│
├── tests/                     # Testes (futuros)
│
├── .env
├── .gitignore
├── main.py                    # Runner da aplicação
├── poetry.lock
├── pyproject.toml
└── README.md

### 🔹 Responsabilidades

- **Controller**  
  Contém a lógica de negócio, validações e fluxo da aplicação.

- **Model**  
  Representa entidades e regras de persistência (PostgreSQL).

- **Route**  
  Camada de exposição da API (FastAPI).

---

## 🔐 Autenticação

A autenticação é feita utilizando **JWT (JSON Web Token)** com os seguintes conceitos:

- **Access Token**
  - Curta duração
  - Usado para acessar rotas protegidas

- **Refresh Token**
  - Longa duração
  - Usado para gerar novos access tokens

### Fluxo de autenticação

1. Usuário faz login
2. Recebe `access_token` e `refresh_token`
3. Access token é enviado no header:

4. Quando o access expira, o refresh é usado
5. Se o refresh expirar → login novamente

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **JWT (python-jose)**
- **OAuth2PasswordBearer**
- **Pydantic**
- **Poetry** (gerenciamento de dependências)

---

## ▶️ Executando o projeto

### 1️⃣ Instalar dependências

```bash
poetry install
poetry shell
uvicorn main:app --reload
```

## A API possui documentação automática via Swagger:
- http://localhost:8000/docs

### Nela é possível:

1. Testar endpoints
2. Realizar login
3. Autorizar via JWT
4. Testar rotas protegidas

## Autor

Projeto desenvolvido por **Gabriel Vilarino**
com foco em aprendizado e prática de backend moderno em Python.