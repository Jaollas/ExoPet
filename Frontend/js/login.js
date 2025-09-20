const API_URL = "http://127.0.0.1:8000/usuarios/login";

document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const senha = document.getElementById("senha").value;


  try {
    const urlComParametros = `${API_URL}?email=${encodeURIComponent(email)}&senha=${encodeURIComponent(senha)}`;

    const response = await fetch(urlComParametros, {
      method: "POST"
    });

    if (!response.ok) throw new Error("Erro no login");

    const data = await response.json();
    document.getElementById("mensagem").textContent = data.message;
    document.getElementById("mensagem").className = "text-success";

    localStorage.setItem("usuario", JSON.stringify(data.usuario));

  } catch (error) {
    console.error("Erro ao fazer login:", error);
    document.getElementById("mensagem").textContent = "Credenciais inválidas.";
    document.getElementById("mensagem").className = "text-danger";
  }
});
