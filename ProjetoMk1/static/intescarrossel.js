const dadosFixos = [
  {
    id: 1,
    titulo: "Painel Solar Residencial",
    descricao: "Sistema de energia solar compacto.",
    imagem: "https://via.placeholder.com/300x200?text=Painel+Solar",
    categoria: "energia"
  },
  {
    id: 2,
    titulo: "Startup de IA",
    descricao: "Inteligência artificial para diagnóstico.",
    imagem: "https://via.placeholder.com/300x200?text=IA+Diagnóstico",
    categoria: "saude"
  },
  {
    id: 3,
    titulo: "Microchip Biotecnológico",
    descricao: "Avanço em tecnologia médica.",
    imagem: "https://via.placeholder.com/300x200?text=Microchip",
    categoria: "tecnologia"
  }
];

// Recupera os dados cadastrados pelo usuário
const dadosUser = JSON.parse(localStorage.getItem("investimentos")) || [];
const todos = [...dadosFixos, ...dadosUser];

todos.forEach(item => {
  const card = document.createElement("div");
  card.classList.add("card");
  card.setAttribute("data-id", item.id);

  card.innerHTML = `
    <img src="${item.imagem}" alt="${item.titulo}" />
    <div class="descricao">
      <h3>${item.titulo}</h3>
      <p>${item.descricao}</p>
    </div>
  `;

  // Animação suave e transição com opacidade
  card.addEventListener("click", () => {
    card.style.transition = "transform 1.2s ease-in-out, opacity 1.2s ease-in-out";
    card.style.transform = "scale(1.2)";
    card.style.opacity = "0.2";
    card.style.pointerEvents = "none"; // impede clique múltiplo

    setTimeout(() => {
      window.location.href = `detalhe.html?id=${item.id}`;
    }, 1200); // espera terminar animação
  });

  // Adiciona ao carrossel correto
  const categoria = item.categoria || "tecnologia";
  const carrossel = document.getElementById(`carrossel-${categoria.toLowerCase()}`);
  if (carrossel) {
    carrossel.appendChild(card);
  }
});
