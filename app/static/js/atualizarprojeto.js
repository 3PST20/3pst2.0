//Atualizar o projeto
document.addEventListener("DOMContentLoaded", function () {
  // Seleciona todos os botões "Atualizar" dentro de elementos com a classe "tab-form"
  const updateButtons = document.querySelectorAll(".tab-form .btn-update");

  updateButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      const form = this.closest("form");
      const formAction = form.getAttribute("action");
      const formId = form.getAttribute("data-form-id");

      fetch(formAction, {
        method: 'PUT',
        body: new URLSearchParams(new FormData(form))
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          alert(data.mensagem);
        })
        .catch(function (error) {
          alert("Erro ao atualizar o projeto. Verifique o console para mais detalhes.");
          console.error(error);
        });
    });
  });
});