const labels = document.querySelectorAll('label')
labels.forEach(element => {
    console.log(element);
    element.remove()
});


const id_direccion = document.getElementById("id_direccion")
id_direccion.setAttribute("placeholder","Direccion")

const id_telefono = document.getElementById("id_telefono")
id_telefono.setAttribute("placeholder","Telefono")

const id_celular = document.getElementById("id_celular")
id_celular.setAttribute("placeholder","Celular")

const id_contraseña = document.getElementById("id_contraseña")
id_contraseña.setAttribute("placeholder","Constraseña")
id_contraseña.setAttribute("type","password")

const id_nit = document.getElementById("id_nit")
id_nit.setAttribute("placeholder","Nit")
id_nit.setAttribute("type","number")

const id_nombre = document.getElementById("id_nombre")
id_nombre.setAttribute("placeholder","Nombre")

const id_correo = document.getElementById("id_correo")
id_correo.setAttribute("placeholder","Correo electronico")

const id_logo = document.getElementById("id_logo")
id_logo.setAttribute("placeholder","Logo")

const id_municipio = document.querySelector("#id_municipio option")
id_municipio.textContent="Municipio"

const id_departamento = document.querySelector("#id_departamento option")
id_departamento.textContent="Departamento"
