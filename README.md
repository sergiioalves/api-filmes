# 🎬 API de Filmes



## 📖 Sobre o projeto

Este projeto implementa uma **API REST em Flask** para o gerenciamento de filmes.  
Faz parte de uma atividade prática sobre **integração contínua (CI/CD)**, boas práticas de commits e automação de testes.

---

## 🚀 Funcionalidades

| Método | Rota | Descrição | Código de retorno |
|--------|-------|------------|-------------------|
| `GET` | `/filmes` | Lista todos os filmes | `200 OK` |
| `GET` | `/filmes/<id>` | Retorna um filme específico | `200 OK` ou `404 Not Found` |
| `DELETE` | `/filmes/<id>` | Remove um filme do catálogo | `204 No Content` ou `404 Not Found` |

---

## ⚙️ Tecnologias utilizadas

- **Python 3.10**
- **Flask**
- **Pytest + Pytest-cov**
- **Flake8**
- **Git + GitHub Actions**

---

## 🧪 Testes e Cobertura

Para rodar os testes localmente:

```bash
pytest --cov=. --disable-warnings -q
```

> 💡 A cobertura mínima exigida é **90%**, validada automaticamente pelo **GitHub Actions**.

---

## 🔄 Integração Contínua (CI/CD)

O repositório utiliza um pipeline automatizado configurado em `.github/workflows/ci.yml`.

### O pipeline executa:
1. ✅ **Verificação de estilo (flake8)**  
   - Garante conformidade com o padrão PEP8.  
2. ✅ **Testes com cobertura (pytest + pytest-cov)**  
   - Falha se a cobertura for menor que 90%.

### Branch protegida:
- A branch principal (`main`) está protegida.
- Apenas merges com pipeline **verde** são permitidos.

---

## 💾 Como executar localmente

Clone o repositório:

```bash
git clone https://github.com/sergiioalves/api-filmes.git
cd api-filmes
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate      # No Windows
# ou
source venv/bin/activate   # No Linux/Mac
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

Acesse no navegador:  
👉 [http://127.0.0.1:5000/filmes](http://127.0.0.1:5000/filmes)

---

## 🧰 Estrutura do projeto

```
api-filmes/
├── app.py
├── requirements.txt
├── tests/
│   └── test_filmes.py
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 🧾 Padrão de commits

O projeto segue o **padrão de commits semânticos**:
- `feat`: nova funcionalidade
- `fix`: correção de bug
- `chore`: tarefas de manutenção
- `style`: ajustes de formatação ou lint

Exemplo:
```bash
git commit -S -m "feat(api): adiciona rota DELETE /filmes/<id>"
```

> 💡 Todos os commits são **assinados com GPG** para garantir autenticidade.

---

## Status

### GitHub Actions
![CI](https://github.com/sergiioalves/api-filmes/actions/workflows/ci.yml/badge.svg)
![Docker Build](https://github.com/sergiioalves/api-filmes/actions/workflows/docker.yml/badge.svg)

### DockerHub
![Docker Hub Version](https://img.shields.io/docker/v/sergioalves1234/api-filmes)
![Docker Pulls](https://img.shields.io/docker/pulls/sergioalves1234/api-filmes)
![Docker Image Size](https://badgen.net/docker/size/sergioalves1234/api-filmes/latest)


## 📚 Autor

**Sérgio Alves**  
🎓 Estudante de Análise e Desenvolvimento de Sistemas   

---

