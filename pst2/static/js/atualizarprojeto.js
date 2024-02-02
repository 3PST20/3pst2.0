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
          window.location.href = '/listarprojeto';
        })
        .catch(function (error) {
          alert("Erro ao atualizar o projeto. Verifique o console para mais detalhes.");
          console.error(error);
        });
    });
  });
});

//Deletar o projeto
document.addEventListener('DOMContentLoaded', function () {
  var btnDelete = document.getElementById('btnDelete');
  if (btnDelete) {
    btnDelete.addEventListener('click', function () {
      var projetoId = btnDelete.getAttribute('data-project-id');
      console.log('projetoId:', projetoId);
      if (projetoId && confirm("Gostaria de excluir o projeto?")) {
        fetch(`/deletaProjeto/${projetoId}`, {
          method: 'DELETE'
        })
          .then(function (response) {
            return response.json();
          })
          .then(function (data) {
            alert(data.mensagem);
            window.location.href = '/listarprojeto';
          })
          .catch(function (error) {
            alert("Erro ao deletar o projeto. Verifique o console para mais detalhes.");
            console.error(error);
          });
      }
    });
  }
});

//Habilitar os campos de edição
function habilitarInput() {
  const inputs = document.querySelectorAll(".form-control, .form-select");
  inputs.forEach(input => {
    input.disabled = false;
  })
  alert("Campos habilitados para edição");
  window.scrollTo({ top: 0, behavior: 'smooth' });

  var btnAlterar = document.getElementById('btnAlterar');
  btnAlterar.disabled = true;
  
  var btnSalvar = document.getElementById('btnSalvar');
  btnSalvar.disabled = false;
}