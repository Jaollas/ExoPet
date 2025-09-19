const API_URL = "http://127.0.0.1:8000/animais/";

async function carregarAnimais() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Erro ao buscar animais");
    const animais = await response.json();

    const container = document.getElementById("animais-container");
    container.innerHTML = "";

    animais.forEach(animal => {
      const card = document.createElement("div");
      card.className = "col-md-4";

      card.innerHTML = `
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">${animal.nome}</h5>
            <p class="card-text"><strong>Espécie:</strong> ${animal.especie}</p>
            <p class="card-text"><strong>Preço:</strong> R$ ${animal.preco}</p>
            <a href="detalhes_animal.html?id=${animal.id}" class="btn btn-primary">Ver detalhes</a>
          </div>
        </div>
      `;
      container.appendChild(card);
    });
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", carregarAnimais);
