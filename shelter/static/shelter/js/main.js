function toggleDiv(divNumber) {
    var div = document.getElementById('toggleDiv' + divNumber);
    var button =document.getElementById('button' + divNumber);
    if (div.style.display === 'none' || div.style.display === '') {
        div.style.display = 'block';
        button.style.transform = 'rotate(90deg)';
    } else {
        div.style.display = 'none';
        button.style.transform = 'rotate(0deg)';
    }
}


