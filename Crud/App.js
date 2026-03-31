let usuarios = [];
let editando = false;
let indiceEditar = -1;
let indiceEliminar = -1;

function login() {
    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("password").value;

    let mensaje = document.getElementById("mensajeLogin");

    if (user === "admin" && pass === "1234") {
        mensaje.textContent = ""; // limpiar mensaje

        document.getElementById("loginContainer").style.display = "none";
        document.getElementById("app").style.display = "block";
    } else {
        mensaje.textContent = "Credenciales incorrectas";
    }
}
 function agregarUsuario() {
    let input = document.getElementById("nombre");
    let nombre = input.value;

    let mensaje = document.getElementById("mensaje");

    if (nombre.trim() === "") {
        mensaje.textContent = "Ingrese un nombre";
        return;
    }

    mensaje.textContent = ""; 

    if (editando) {
        usuarios[indiceEditar] = nombre;
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
    indiceEliminar = index;
    document.getElementById("confirmModal").style.display = "block";
}

function confirmarEliminar() {
    usuarios.splice(indiceEliminar, 1);
    mostrarUsuarios();
    cerrarModal();
}

function cerrarModal() {
    document.getElementById("confirmModal").style.display = "none";
}

function editarUsuario(index) {
    let input = document.getElementById("nombre");

    input.value = usuarios[index];
    editando = true;
    indiceEditar = index;
}