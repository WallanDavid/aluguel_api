# 🏠 Sistema de Aluguel de Imóveis - API + Admin

Projeto fullstack desenvolvido com **FastAPI** no backend e **Vite + React + Tailwind** no frontend (admin). Inspirado no estilo de APIs públicas como o ViaCEP, com uma interface administrativa enxuta para gerenciar imóveis, usuários e contratos de aluguel.

---

## 🚀 Tecnologias

### Backend:
- ⚙️ **Python 3.11+**
- ⚡ **FastAPI**
- 🐘 **PostgreSQL** (ou SQLite, a depender da config)
- 🔐 **JWT** (Autenticação)
- 🧰 **Uvicorn**, **Pydantic**, **SQLAlchemy**

### Frontend:
- ⚛️ **React 18+**
- ⚡ **Vite**
- 💨 **Tailwind CSS**
- 🧭 **React Router DOM**

---

## 🧩 Funcionalidades

### API
- [x] Autenticação com login e token JWT
- [x] CRUD completo:
  - 🧑 Usuários
  - 🏢 Imóveis
  - 📄 Contratos

### Painel Admin
- [x] Login de administrador
- [x] Painel com layout fixo (sidebar e navbar)
- [x] Listagem e criação (CRUD visual em progresso)
- [ ] Validações, melhorias visuais e integrações completas com API

---

## 🔧 Como rodar localmente

### Backend (FastAPI)
```bash
# Ative o virtualenv se ainda não fez:
venv\Scripts\activate

# Inicie o servidor
uvicorn main:app --reload
