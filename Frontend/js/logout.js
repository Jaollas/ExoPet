const API_URL = "http://127.0.0.1:8000/usuarios/logout";

document.getElementById("logout-btn").addEventListener("click", async () => {
  try {
    const response = await fetch(API_URL, { method: "POST" });
    const data = await response.json();

    document.getElementById("mensagem").textContent = data.message;
    document.getElementById("mensagem").className = "text-success";

    // Limpar sessão local
    localStorage.removeItem("usuario");

  } catch (error) {
    document.getElementById("mensagem").textContent = "Erro ao realizar logout.";
    document.getElementById("mensagem").className = "text-danger";
  }
});
