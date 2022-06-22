const labels = document.querySelectorAll('label')
labels.forEach(element => {
    console.log(element);
    element.remove()
});

const nombre = document.getElementById("id_nombre")

nombre.setAttribute("placeholder","Nombre")
