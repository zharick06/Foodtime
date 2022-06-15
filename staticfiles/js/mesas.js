
const btns = document.querySelectorAll('#btn')
btns.forEach(element => {
    console.log(element);
    if (element.textContent != "Desactivar") {
        console.log(element.textContent);
        element.style.background = 'Grey';
    }
});



