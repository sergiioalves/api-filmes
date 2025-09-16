const express = require("express");
const app = express();
const PORT = 8080;

app.use(express.json());

let filmes = [
  { id: 1, titulo: "O Poderoso Chefão", ano: 1972 },
  { id: 2, titulo: "Clube da Luta", ano: 1999 },
  { id: 3, titulo: "A Origem", ano: 2010 }
];

app.get("/api/filmes", (req, res) => {
  res.json(filmes);
});

app.post("/api/filmes", (req, res) => {
  const { titulo, ano } = req.body;

  if (!titulo || !ano) {
    return res.status(400).json({ error: "Título e ano são obrigatórios" });
  }

  const novoFilme = {
    id: filmes.length + 1,
    titulo,
    ano
  };

  filmes.push(novoFilme);
  res.status(201).json(novoFilme);
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
