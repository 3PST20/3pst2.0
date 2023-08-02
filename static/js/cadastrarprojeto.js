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