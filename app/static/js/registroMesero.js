const labels = document.querySelectorAll('label')
labels.forEach(element => {
    element.setAttribute("class", "block mb-2 text-sm font-bold text-gray-700")
});

const id_foto = document.getElementById('id_foto')
id_foto.setAttribute("class", "block mb-2 text-sm font-bold text-gray-700")

const id_usuario = document.getElementById("id_usuario")
id_usuario.setAttribute("placeholder","Usuario")
id_usuario.setAttribute("class","w-60 px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_contraseña = document.getElementById("id_contraseña")
id_contraseña.setAttribute("placeholder","Constraseña")
id_contraseña.setAttribute("type","password")
id_contraseña.setAttribute("class","w-60 px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_documento = document.getElementById("id_documento")
id_documento.setAttribute("placeholder","Documento")
id_documento.setAttribute("class", "w-60 px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_tipodocOp = document.querySelector("#id_tipodoc option")
id_tipodocOp.textContent="Tipo documento"
id_tipodocOp.setAttribute("id","opcion_predeterminada")
const id_tipodoc = document.querySelector("#id_tipodoc")
id_tipodoc.setAttribute("class", "w-60 px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_nombre1 = document.getElementById("id_nombres")
id_nombre1.setAttribute("placeholder","Nombres")
id_nombre1.setAttribute("class", "w-60 px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_apellido1 = document.getElementById("id_apellidos")
id_apellido1.setAttribute("placeholder","Apellidos")
id_apellido1.setAttribute("class", "w-60 px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_correo = document.getElementById("id_correo")
id_correo.setAttribute("placeholder","Correo electronico")
id_correo.setAttribute("class", "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_telefono = document.getElementById("id_telefono")
id_telefono.setAttribute("placeholder","Telefono")
id_telefono.setAttribute("class", "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_generoOp = document.querySelector("#id_genero option")
id_generoOp.textContent="Genero"
const id_genero = document.querySelector("#id_genero")
id_genero.setAttribute("class", "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_direccion = document.getElementById("id_direccion")
id_direccion.setAttribute("placeholder","Direccion")
id_direccion.setAttribute("class", "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")

const id_municipioOp = document.querySelector("#id_municipio option")
id_municipioOp.textContent="Municipio"
const id_municipio = document.querySelector("#id_municipio")
id_municipio.setAttribute("class", "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline")




