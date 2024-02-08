//Habilitar os campos de edição
/**
 * A função `habilitarInput()` habilita todos os campos de entrada de um formulário e 
 * desabilita o botão "Alterar" ao ativar o botão "Salvar".
 * @date 2024-02-07 
 * @author Ana Carolina
 */
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