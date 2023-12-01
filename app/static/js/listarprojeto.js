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

function htmlToCsv(filename){
    var data = []
    var rows = document.querySelectorAll("table tr")

    for(var i=0; i<rows.length; i++){
        var row = [], cols = rows[i].querySelectorAll("td, th")

        for(var j=0; j<cols.length; j++){
            row.push(cols[j].innerText)
        }
        data.push(row.join(","))
    }

    downloadCSVFile(data.join("\n"), filename)
}

function downloadCSVFile(csv, filename){
    var csv_file, download_link
    csv_file = new Blob([csv], {type: "text/csv"});
    download_link = document.createElement("a")
    download_link.download = filename
    download_link.href = window.URL.createObjectURL(csv_file)
    download_link.style.display = "none"
    document.body.appendChild(download_link)
    download_link.click()
}