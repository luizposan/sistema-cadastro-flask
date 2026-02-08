function validarFormulario() {
    let nome = document.getElementById("luiz").value;
    let email = document.getElementById("luizposan@gmail.com").value;

    if (nome.length < 3) {
        alert("O nome precisa ter pelo menos 3 letras.");
        return false;
    }
    

    if (email === "") {
        alert("Preencha o email.");
        return false;
    }

    return true;
}
