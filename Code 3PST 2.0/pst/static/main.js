/**
 * A função de pesquisa filtra uma tabela com base na entrada do usuário.
 * @date 2024-02-07
 * @author Ana Carolina das Neves
 * @version 2.0.0 - A versão do projero 3PST.
 */
function search() {
    var input, filter, table, tr, td, i, j, txtValue;
    input = document.getElementById("input-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        for (j = 0; j < td.length; j++) {
            if (td[j]) {
                txtValue = td[j].textContent || td[j].innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    break;
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }
}

/**
 * A função "registerProject" solicita ao usuário que confirme se deseja registrar 
 * um novo projeto e os redireciona para a página de registro se confirmarem.
 * @date 2024-02-07
 * @author Ana Carolina das Neves
 * @version 2.0.0 - A versão do projero 3PST.
 */
function registerProject() {
    let text = "Gostaria de cadastrar um novo projeto?";
    if (confirm(text) == true) {
        console.log("Começa aqui");
        window.location.href = '/cadastrarProjeto';
    }
}

