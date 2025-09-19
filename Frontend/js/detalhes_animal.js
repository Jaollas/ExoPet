const API_URL = "http://127.0.0.1:8000/animais/";

function getIdFromUrl() {
  const params = new URLSearchParams(window.location.search);
  return params.get("id");
}

async function carregarDetalhes() {
  const id = getIdFromUrl();
  if (!id) return;

  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Erro ao buscar animais");
    const animais = await response.json();

    const animal = animais.find(a => a.id == id);
    if (!animal) {
      document.getElementById("detalhes-container").innerHTML = "<p>Animal não encontrado.</p>";
      return;
    }

    const container = document.getElementById("detalhes-container");
    container.innerHTML = `
      <h2>${animal.nome}</h2>
      <p><strong>Espécie:</strong> ${animal.especie}</p>
      <p><strong>Descrição:</strong> ${animal.descricao}</p>
      <p><strong>Preço:</strong> R$ ${animal.preco}</p>
      <p><strong>Dono:</strong> ${animal.dono_id}</p>
    `;
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", carregarDetalhes);
