const API_URL = "http://127.0.0.1:8000/usuarios/";

document.getElementById("usuario-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const usuario = {
    nome: document.getElementById("nome").value,
    email: document.getElementById("email").value,
    senha: document.getElementById("senha").value
  };

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(usuario)
    });

    const data = await response.json();
    document.getElementById("mensagem").textContent = data.message || "Usuário cadastrado!";
    document.getElementById("mensagem").className = "text-success";
  } catch (error) {
    document.getElementById("mensagem").textContent = "Erro ao cadastrar usuário.";
    document.getElementById("mensagem").className = "text-danger";
  }
});
