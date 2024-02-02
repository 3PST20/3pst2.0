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

function registerProject() {
    let text = "Gostaria de cadastrar um novo projeto?";
    if (confirm(text) == true) {
        console.log("Começa aqui");
        fetch('/cadastroProjeto', {
            method: 'POST'
        })
            .then(response => response.json())
            .then(json => {
                console.log(JSON.stringify(json));
            
                // Verificar se o ID do projeto está presente na resposta JSON
                if (json.projeto && json.projeto.projeto && json.projeto.projeto.id) {
                    const projetoId = json.projeto.projeto.id;
                    console.log("Projeto ID:", projetoId);
            
                    // Construir a URL de redirecionamento
                    const redirectURL = `/novoProjeto/${projetoId}`;
                    console.log("Redirecionando para:", redirectURL);
            
                    // Redirecionar para a tela de cadastro do projeto recém-criado
                    window.location.href = redirectURL;
                } else {
                    console.error("ID do projeto ausente na resposta JSON");
                }
            })            
            .catch(error => {
                alert("Erro ao cadastrar o projeto. Verifique o console para mais detalhes.");
                console.error(error);
            });
    }
}

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