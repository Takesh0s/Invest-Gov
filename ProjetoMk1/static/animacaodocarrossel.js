function aplicarAnimacaoClique(card) {
    card.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
    card.style.transform = 'scale(1.2)';
    card.style.opacity = '0';
    setTimeout(() => {
      const id = card.getAttribute("data-id");
      navegarParaDetalhes(id);
    }, 400);
  }
  