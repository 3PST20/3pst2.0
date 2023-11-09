//1. Deselicionar a 'aba' active
//2. Reconhecer click
//3. Ativar a 'aba' clicada
//4. Esconder as informações da 'aba' active
//5. Ativar as informações da 'aba' clicada
//6. Salvar e cancelar por 'aba'


function changeTabContent(tabIndex) {
  // Esconder todos os conteúdos das abas
  var tabContents = document.querySelectorAll("#tabContent > div");
  for (var i = 0; i < tabContents.length; i++) {
    tabContents[i].style.display = "none";
  }

  // Mostrar o conteúdo da aba selecionada
  var selectedContent = document.getElementById("content" + tabIndex);
  if (selectedContent) {
    selectedContent.style.display = "block";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  // Seleciona todos os botões "Salvar" dentro de elementos com a classe "tab-form"
  const salvarButtons = document.querySelectorAll(".tab-form .btn-success");

  salvarButtons.forEach(function (button) {
      button.addEventListener("click", function () {
          const form = this.closest("form");
          const formAction = form.getAttribute("data-form-action");
          const formId = form.getAttribute("data-form-id");

          fetch(formAction, {
              method: form.method,
              body: new URLSearchParams(new FormData(form))
          })
          .then(function (response) {
              return response.json();
          })
          .then(function (data) {
              alert(data.mensagem);
              form.reset();
          })
          .catch(function (error) {
              alert("Erro ao cadastrar o projeto. Verifique o console para mais detalhes.");
              console.error(error);
          });
      });
  });
});