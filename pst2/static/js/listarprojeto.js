/**
 * A função de pesquisa filtra uma tabela com base na entrada do usuário.
 * @date 2024-02-07
 * @author Ana Carolina
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
 * @author Ana Carolina
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
 * @date 2024-02-07
 * @author Ana Carolina
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
 * @date 2024-02-07
 * @author Ana Carolina
 * @param { string } csv - O parâmetro `csv` é uma string que representa o conteúdo do arquivo CSV que você deseja baixar.
 * @param { string } filename - O parâmetro 'filename' é uma string que especifica o nome do arquivo a ser baixado.
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