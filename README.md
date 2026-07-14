# 🦇 Wayne Industries — Sistema de Gestão Interna

Sistema web full stack desenvolvido como projeto final do curso **Dev Full Stack** da Infinity School.

A plataforma simula o sistema interno das **Indústrias Wayne**, permitindo controle de acesso por níveis de usuário, gerenciamento de recursos e um painel de visualização com dados em tempo real.

---

## 🚀 Funcionalidades

### 🔐 Autenticação e Controle de Acesso
- Login seguro com senha criptografada (Werkzeug)
- Três níveis de acesso: **Administrador**, **Gerente** e **Funcionário**
- Rotas protegidas — acesso negado para usuários não autorizados
- Sessões gerenciadas com Flask-Login

### 📦 Gestão de Recursos
- Cadastro de equipamentos, veículos e dispositivos de segurança
- Edição e remoção de recursos
- Filtros por categoria e status
- Status: Disponível, Em Manutenção, Em Campo

### 📊 Dashboard
- Painel com contadores em tempo real
- Listagem dos recursos mais recentes
- Visão geral de usuários e recursos cadastrados

### 👥 Gestão de Usuários _(somente Admin)_
- Criação de novos usuários com definição de papel
- Edição de dados e senha
- Remoção de usuários (com proteção contra auto-remoção)

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python + Flask |
| Banco de Dados | SQLite + SQLAlchemy |
| Autenticação | Flask-Login + Werkzeug |
| Frontend | HTML5 + CSS3 + JavaScript |
| Templates | Jinja2 |

---

## 📁 Estrutura do Projeto

```
wayne-industries/
├── app.py                  # Ponto de entrada da aplicação
├── extensions.py           # Instâncias do SQLAlchemy e LoginManager
├── models.py               # Modelos do banco de dados (User, Resource)
├── routes/
│   ├── __init__.py
│   ├── auth.py             # Login e logout
│   ├── dashboard.py        # Painel de controle
│   ├── resources.py        # CRUD de recursos
│   └── users.py            # CRUD de usuários
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── resources.html
│   ├── resource_form.html
│   ├── users.html
│   └── user_form.html
└── static/                 # Arquivos estáticos (CSS, JS)
```

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos
- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Joaopaulomelo1/Projeto-Fullstack-Industrias-wayne-.git
cd wayne-industries

# Instale as dependências
pip install flask flask-sqlalchemy flask-login

# Rode o servidor
python app.py
```

Acesse em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Credenciais padrão

| Usuário | Senha | Papel |
|---------|-------|-------|
| bruce.wayne | gotham123 | Administrador |

> O usuário admin é criado automaticamente no primeiro acesso.

---

## 🔒 Níveis de Acesso

| Funcionalidade | Funcionário | Gerente | Admin |
|----------------|:-----------:|:-------:|:-----:|
| Ver Dashboard | ✅ | ✅ | ✅ |
| Ver Recursos | ✅ | ✅ | ✅ |
| Adicionar/Editar Recursos | ❌ | ✅ | ✅ |
| Remover Recursos | ❌ | ✅ | ✅ |
| Gerenciar Usuários | ❌ | ❌ | ✅ |

---

## 📌 Sobre o Projeto

Desenvolvido como projeto final do curso **Dev Full Stack** da Infinity School, utilizando os conhecimentos adquiridos ao longo do curso: Python, HTML, CSS, JavaScript e bibliotecas como Flask e SQLAlchemy.

---

## 👤 Autor

Feito por **João Paulo Melo** — [GitHub] https://github.com/Joaopaulomelo1
