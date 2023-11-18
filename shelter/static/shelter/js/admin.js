function toggleDivs() {
    var div1 = document.getElementById('div1');
    var div2 = document.getElementById('div2');

    if (div1.style.display !== 'none') {
        div1.style.display = 'none';
        div2.style.display = 'block';
    } else {
        div1.style.display = 'block';
        div2.style.display = 'none';
    }
}

function resizeTextarea() {
    var textarea = document.getElementById('resizableTextarea');
    textarea.style.height = 'auto'; // Спочатку встановлюємо автоматичну висоту для скидання попередньо встановленої висоти
    textarea.style.height = textarea.scrollHeight + 'px'; // Встановлюємо висоту, щоб вміст вміщувався
}

function reloadPage() {
// Викликаємо метод перезавантаження сторінки
    location.reload();
}