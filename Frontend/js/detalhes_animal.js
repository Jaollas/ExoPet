const API_URL = "http://127.0.0.1:8000/animais";

function getIdFromUrl() {
  const params = new URLSearchParams(window.location.search);
  return params.get("id");
}

async function carregarDetalhes() {
  const id = getIdFromUrl();
  if (!id) return;

  try {
    const response = await fetch(`${API_URL}/${id}`);
    if (!response.ok) throw new Error("Erro ao buscar detalhes do animal");
    const animal = await response.json();

    const container = document.getElementById("detalhes-container");
    container.innerHTML = `
      <h2>${animal.nome}</h2>
      <p><strong>Espécie:</strong> ${animal.especie}</p>
      <p><strong>Descrição:</strong> ${animal.descricao}</p>
      <p><strong>Preço:</strong> R$ ${animal.preco}</p>
      <p><strong>Dono (ID):</strong> ${animal.dono_id}</p>
    `;
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", carregarDetalhes);
