# 🎬 API de Filmes

API REST simples feita em **Node.js + Express**, com duas funcionalidades principais:

* **Feature 1**: Rota `GET /api/filmes` → retorna a lista de filmes.
* **Feature 2**: Rota `POST /api/filmes` → permite adicionar um novo filme.

---

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/sergiioalves/api-filmes.git
cd api-filmes
```

### 2. Instalar dependências

```bash
npm install
```

### 3. Rodar a API

```bash
npm start
```

---

## 📌 Testando a API

### GET - Listar filmes

**Rota:**

```
GET http://localhost:8080/api/filmes
```

**Exemplo de resposta:**

```json
[
  { "id": 1, "titulo": "O Poderoso Chefão", "ano": 1972 },
  { "id": 2, "titulo": "Clube da Luta", "ano": 1999 },
  { "id": 3, "titulo": "A Origem", "ano": 2010 }
]
```

---

### POST - Adicionar novo filme

**Rota:**

```
POST http://localhost:8080/api/filmes
```

**Exemplo de corpo (JSON):**

```json
{
  "titulo": "Matrix",
  "ano": 1999
}
```

**Exemplo de resposta:**

```json
{
  "id": 4,
  "titulo": "Matrix",
  "ano": 1999
}
```

> Obs: Tanto o `titulo` quanto o `ano` são obrigatórios. Caso falte algum, a API retorna um erro 400.

---

## 🔄 Workflow adotado

Optei por um **workflow baseado em trunk (branch main)**:

* Todas as features foram implementadas diretamente na branch `main`.
* Esse fluxo é simples e direto, adequado para projetos pequenos e de aprendizado.
* Em projetos maiores, seria interessante usar **Git Flow** ou **GitHub Flow** para melhor organização.

---

## 🛠 Tecnologias utilizadas

* Node.js
* Express

---

