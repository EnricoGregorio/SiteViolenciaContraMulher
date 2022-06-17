//Funções JQuery
$(function() {
    // Função para quando pressionar o botão do menu, ele faça algo.
    $(".menu-button").click(function() {
        const menuMobile = $('nav.mobile');
        if (menuMobile.is(':hidden') == false) {
            menuMobile.slideToggle();
            window.document.querySelector(".fa-bars").style.display = 'block';
            window.document.querySelector(".fa-times").style.display = 'none';
        } else {
            menuMobile.slideToggle();
            window.document.querySelector(".fa-bars").style.display = 'none';
            window.document.querySelector(".fa-times").style.display = 'block';
        }
    });
});

// Comando para deixar o ícone X do menu de navegação 'escondido' por padrão.
window.document.querySelector(".fa-times").style.display = 'none';