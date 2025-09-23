const API_URL_USERS = "http://127.0.0.1:8000/usuarios";
const API_URL_ANIMAIS = "http://127.0.0.1:8000/animais";

async function carregarUsuario() {
  const userId = localStorage.getItem("userId");
  if (!userId) {
    window.location.href = "login.html";
    return;
  }

  try {
    const respUser = await fetch(`${API_URL_USERS}/${userId}`);
    const usuario = await respUser.json();

    document.getElementById("dados-usuario").innerHTML = `
      <p><strong>ID:</strong> ${usuario.id}</p>
      <p><strong>Nome:</strong> ${usuario.nome}</p>
      <p><strong>Email:</strong> ${usuario.email}</p>
    `;

    const respPets = await fetch(`${API_URL_ANIMAIS}?dono_id=${userId}`);
    const pets = await respPets.json();

    const container = document.getElementById("meus-pets");
    container.innerHTML = "";

    pets.forEach(pet => {
      const col = document.createElement("div");
      col.className = "col-md-4";

      col.innerHTML = `
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">${pet.nome}</h5>
            <p><strong>Espécie:</strong> ${pet.especie}</p>
            <p><strong>Descrição:</strong> ${pet.descricao}</p>
            <p><strong>Preço:</strong> R$ ${pet.preco}</p>
            <button class="btn btn-warning me-2" onclick="editarPet(${pet.id})">Editar</button>
            <button class="btn btn-danger" onclick="removerPet(${pet.id})">Excluir</button>
          </div>
        </div>
      `;
      container.appendChild(col);
    });

  } catch (err) {
    console.error(err);
  }
}

async function editarPet(id) {
  const userId = localStorage.getItem("userId");
  const novoNome = prompt("Novo nome do pet:");
  if (!novoNome) return;

  try {
    await fetch(`${API_URL_ANIMAIS}/${id}?usuario_id=${userId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome: novoNome })
    });
    alert("Pet atualizado!");
    carregarUsuario();
  } catch (err) {
    console.error(err);
  }
}

async function removerPet(id) {
  const userId = localStorage.getItem("userId");
  if (!confirm("Deseja realmente excluir este pet?")) return;

  try {
    await fetch(`${API_URL_ANIMAIS}/${id}?usuario_id=${userId}`, {
      method: "DELETE"
    });
    alert("Pet removido!");
    carregarUsuario();
  } catch (err) {
    console.error(err);
  }
}

document.addEventListener("DOMContentLoaded", carregarUsuario);
