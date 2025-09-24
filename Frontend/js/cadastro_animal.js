const API_URL = "http://127.0.0.1:8000/animais/";

document.getElementById("animal-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const animal = {
    nome: document.getElementById("nome").value,
    especie: document.getElementById("especie").value,
    descricao: document.getElementById("descricao").value,
    preco: parseFloat(document.getElementById("preco").value),
    dono_id: parseInt(localStorage.getItem("userId"))
  };

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(animal)
    });

    const data = await response.json();
    document.getElementById("mensagem").textContent = data.message || "Animal cadastrado!";
    document.getElementById("mensagem").className = "text-success";
  } catch (error) {
    document.getElementById("mensagem").textContent = "Erro ao cadastrar animal.";
    document.getElementById("mensagem").className = "text-danger";
  }
});
