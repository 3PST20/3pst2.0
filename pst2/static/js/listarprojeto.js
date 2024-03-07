// ---------------------------------------------------------
// INPE/COGPI/SEPEC - Serviço de Planejamento e Controle
// ---------------------------------------------------------
// Versão 3PST 2.0.0
// Módulo I
//
// Ferrementa JSDoc 4.0.2
//---------------- Integrantes do Projeto 3PST -------------
// Alberto de Paula Silva
// Ana Carolina das Neves
// Ane Caroline Maciel de Lima
// Bárbara Alessandra Gonçalves Pinheiro Yamada
// Renato Henrique Ferreira Branco
// Viviane Ferreira da Silva de Macedo
//
//---------------- Histórico de Revisão --------------------
//      Nome                      Data
// Ana Carolina das Neves          05/02/2024   


/**
 * A função de pesquisa filtra uma tabela com base na entrada do usuário.
 * @date 2023-12-01
 * @author Ana Carolina das Neves
 * @version 3PST-2.0.0 - A versão do projero 3PST.
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
 * @date 2023-12-01
 * @author Ana Carolina Neves
 * @version 3PST-2.0.0 - A versão do projero 3PST.
 */
function registerProject() {
    let text = "Gostaria de cadastrar um novo projeto?";
    if (confirm(text) == true) {
        console.log("Começa aqui");
        window.location.href = '/cadastrarprojeto';
    }
}

/**
 * A função `htmlToCsv` converte uma tabela HTML em um arquivo CSV e faz o download.
 * @date 2023-12-01
 * @author Ana Carolina das Neves
 * @version 3PST-2.0.0 - A versão do projero 3PST.
 * @param { string } filename - O parâmetro `filename` é uma string que representa 
 * o nome do arquivo CSV que será baixado.
 */
function htmlToCsv(filename) {
    var data = []
    var rows = document.querySelectorAll("table tr")

    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th")

        for (var j = 0; j < cols.length; j++) {
            row.push(cols[j].innerText)
        }
        data.push(row.join(","))
    }

    downloadCSVFile(data.join("\n"), filename)
}

/**
 * A função `downloadCSVFile` é responsável por criar um arquivo CSV e iniciar seu download.
 * @date 2023-12-01
 * @author Ana Carolina das Neves
 * @version 3PST-2.0.0 - A versão do projero 3PST.
 * @param { string } csv - O parâmetro `csv` é uma string que representa o conteúdo do arquivo CSV que você deseja baixar.
 * @param { string } filename - O parâmetro 'filename' é uma string que especifica o nome do arquivo a ser baixado.
 * @param { string } tagname - Cria uma instância do elemento para a tag especificada.
 */
function downloadCSVFile(csv, filename) {
    var csv_file, download_link
    csv_file = new Blob([csv], { type: "text/csv" });
    download_link = document.createElement("a") 
    download_link.download = filename
    download_link.href = window.URL.createObjectURL(csv_file)
    download_link.style.display = "none"
    document.body.appendChild(download_link)
    download_link.click()
}