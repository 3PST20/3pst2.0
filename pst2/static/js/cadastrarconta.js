document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("btnSalvar");

    button.addEventListener("click", function (event) {
        event.preventDefault();

        const form = this.closest("form");
        const formAction = form.getAttribute("data-form-action");
        const formId = form.getAttribute("data-form-id");

        fetch(formAction, {
            method: form.method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nome: form.querySelector('[name="nome"]').value,
                email: form.querySelector('[name="email"]').value,
                tipoUsuario: form.querySelector('[name="tipoUsuario"]').value,
                senha: form.querySelector('[name="senha"]').value
            })
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            alert(data.mensagem);
            form.reset();
        })
        .catch(function (error) {
            alert("Erro ao cadastrar o usuário. Verifique o console para mais detalhes.");
            console.error(error);
        });
    });
});
