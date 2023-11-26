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







/// оновлення фото під час додавання у форму
function previewImage(input) {
    var preview = document.getElementById('imagePreview');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    };

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "#";
    }
}

function submitForm() {
 // You can add additional validation or processing here
    document.getElementById('animalForm').submit();
}