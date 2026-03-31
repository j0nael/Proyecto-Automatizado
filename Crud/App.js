let usuarios = [];
let editando = false;
let indiceEditar = -1;

function login() {
    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("password").value;

    if (user === "admin" && pass === "1234") {
        document.getElementById("loginContainer").style.display = "none";
        document.getElementById("app").style.display = "block";
    } else {
        alert("Credenciales incorrectas");
    }
}

function agregarUsuario() {
    let input = document.getElementById("nombre");
    let nombre = input.value;

   if (nombre.trim() === "") {
        alert("Ingrese un nombre");
        return;
    }

    if (editando) {
       usuarios[indiceEditar] = nombre + " (editado)";
        editando = false;
        indiceEditar = -1;
    } else {
        usuarios.push(nombre);
    }

    input.value = "";
    mostrarUsuarios();
}

function mostrarUsuarios() {
    let lista = document.getElementById("listaUsuarios");
    lista.innerHTML = "";

    usuarios.forEach((usuario, index) => {
        let li = document.createElement("li");

        li.innerHTML = `
            ${usuario}
            <button onclick="editarUsuario(${index})">Editar</button>
            <button onclick="eliminarUsuario(${index})">Eliminar</button>
        `;

        lista.appendChild(li);
        
    });
    let contador = document.getElementById("contador");
contador.textContent = "Total usuarios: " + usuarios.length;
}

function eliminarUsuario(index) {
    if (confirm("¿Seguro que quieres eliminar?")) {
        usuarios.splice(index, 1);
        mostrarUsuarios();
    }
}

function editarUsuario(index) {
    let input = document.getElementById("nombre");

    input.value = usuarios[index];
    editando = true;
    indiceEditar = index;
}