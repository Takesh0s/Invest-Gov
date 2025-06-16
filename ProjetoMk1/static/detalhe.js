// detalhe.js

const params = new URLSearchParams(window.location.search);
const id = parseInt(params.get("id"));

const dados = JSON.parse(localStorage.getItem("investimentos")) || [];

const item = dados.find(i => i.id === id);

if (item) {
  document.getElementById("detalhe-imagem").src = item.imagem;
  document.getElementById("detalhe-titulo").textContent = item.titulo;
  document.getElementById("detalhe-texto").textContent = item.descricao;
} else {
  document.body.innerHTML = "<h2>Produto não encontrado.</h2>";
}
