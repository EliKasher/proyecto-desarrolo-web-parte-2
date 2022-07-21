function fechaTermino(){
    var date = new Date();
    year = date.getFullYear();
    month = (date.getMonth() + 1).toString().padStart(2,'0');
    day = date.getDate().toString().padStart(2, '0');
    hours = date.getHours(date.setHours(date.getHours() + 3)).toString().padStart(2, '0');
    minutes = date.getMinutes().toString().padStart(2, '0');
    document.getElementById("dia-hora-termino").value = year + "-" + month + "-" + day + " " + hours + ":" + minutes;
}

function fechaInicio(){
    var date = new Date();
    year = date.getFullYear();
    month = (date.getMonth() + 1).toString().padStart(2,'0');
    day = date.getDate().toString().padStart(2,'0');
    hours = date.getHours().toString().padStart(2,'0');
    minutes = date.getMinutes().toString().padStart(2,'0');
    document.getElementById("dia-hora-inicio").value = year + "-" + month + "-" + day + " " + hours + ":" + minutes;
}