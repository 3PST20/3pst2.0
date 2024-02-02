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