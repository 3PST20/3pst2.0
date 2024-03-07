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


//Habilitar os campos de edição

/**
 * A função `habilitarInput()` habilita todos os campos de entrada de um formulário e 
 * desabilita o botão "Alterar" ao ativar o botão "Salvar".
 * @date 2024-02-02 
 * @author Ana Carolina das Neves
 * @version 3PST-2.0.0 - A versão do projero 3PST.
 * @param {string} elemenId - Retorna uma referência ao primeiro objeto com o valor especificado 
 * do atributo ID.
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