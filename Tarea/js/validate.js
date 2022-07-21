function validate() {
    let region = document.getElementById('region').value;
    let comuna = document.getElementById('comuna').value;
    let sector = document.getElementById('sector').value.length;
    let nombre = document.getElementById('nombre').value.length;
    let email = document.getElementById('email').value;
    let celular = document.getElementById('celular').value;
    let contacto = document.getElementById('contacto');
    let tema = document.getElementById('tema').value;
    let otroTema = document.getElementById('otroTema');
    let foto = document.getElementById('foto-actividad').value;
    let fechaInicio = document.getElementById('dia-hora-inicio').value;
    let fechaFinal = document.getElementById('dia-hora-termino').value;

    let errors = '';

    if (!validarRegion(region)){
        document.getElementById('region').style.backgroundColor = "#a33c638c";
        errors += '<p>Ingrese región</p>';
    } else{
        document.getElementById('region').style.backgroundColor = "white";
    }

    if (!validarComuna(comuna)){
        document.getElementById('comuna').style.backgroundColor = "#a33c638c";
        errors += '<p>Ingrese comuna</p>';
    } else{
        document.getElementById('comuna').style.backgroundColor = "white";
    }

    if (!validarSector(sector)){
        document.getElementById('sector').style.backgroundColor = "#a33c638c";
        errors += '<p>Superó el largo permitido</p>';
    } else{
        document.getElementById('sector').style.backgroundColor = "white";
    }

    if (!validarNombre(nombre)){
        document.getElementById('nombre').style.backgroundColor = "#a33c638c";
        errors += '<p>El nombre está mal</p>';
    } else{
        document.getElementById('nombre').style.backgroundColor = "white";
    }

    if (!validarEmail(email)){
        document.getElementById('email').style.backgroundColor = "#a33c638c";
        errors += '<p>El correo está mal</p>';
    } else{
        document.getElementById('email').style.backgroundColor = "white";
    }

    if (!validarCelular(celular)){
        document.getElementById('celular').style.backgroundColor = "#a33c638c";
        errors += '<p>El celular está mal</p>';
    } else{
        document.getElementById('celular').style.backgroundColor = "white";
    }

    if (!validarContacto(contacto)){
        document.getElementById('contacto').style.backgroundColor = "#a33c638c";
        errors += '<p>El url de contacto está mal</p>';
    } else if (contacto != null){
        document.getElementById('contacto').style.backgroundColor = "white";
    }

    if (!validarTema(tema)){
        document.getElementById('tema').style.backgroundColor = "#a33c638c";
        errors += '<p>Debe elegir al menos 1 tema</p>';
    } else{
        document.getElementById('tema').style.backgroundColor = "white";
    }

    if (!validarOtro(otroTema)){
        document.getElementById('otroTema').style.backgroundColor = "#a33c638c";
        errors += '<p>Debe elegir al menos 1 tema</p>';
    } else if(otroTema != null){
        document.getElementById('otroTema').style.backgroundColor = "white";
    }

    if (!validarFechaInicial(fechaInicio)){
        document.getElementById('dia-hora-inicio').style.backgroundColor = "#a33c638c";
        errors += '<p>Debe elegir una fecha válida</p>';
    } else{
        document.getElementById('dia-hora-inicio').style.backgroundColor = "white";
    }

    if (!validarFechaFinal(fechaFinal)){
        document.getElementById('dia-hora-termino').style.backgroundColor = "#a33c638c";
        errors += '<p>Debe elegir una fecha válida</p>';
    } else{
        document.getElementById('dia-hora-termino').style.backgroundColor = "white";
    }

    if (!validarFoto(foto)){
        document.getElementById('foto-actividad').style.backgroundColor = "#a33c638c";
        errors += '<p>Debe elegir al menos 1 foto</p>';
    } else{
        document.getElementById('foto-actividad').style.backgroundColor = "#022a2a5b";

    }

    /*Finalmente si hay errores lo escribimos en el contenedor de errores, en nuestro div al costado del formulario*/
    if(errors != ''){
        document.getElementById('contenedorErrores').innerHTML = errors;
        return false;
    }
    
    return true;
}

function validarRegion(region){

    if(region == 'sin-region'){
        return false;
    }

    return true;

}

function validarComuna(comuna){

    if(comuna == 'sin-comuna' | comuna == 'sin-region'){
        return false;
    }

    return true;

}

function validarSector(sector){
    if(sector > 100){
        return false;
    }

    return true;

}

function validarNombre(nombre){
    if(nombre == 0 | nombre > 200){
        return false;
    }

    return true;

}

function validarEmail(email){
    let emailRegEx = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

    if(!emailRegEx.test(email) | email == '') {
        return false;
    }
    return true;
}

function validarCelular(celular){
    let cellRegEx = /([+56][ ][2-9])[ ](\d{4})(\d{4})/g;
    if (celular != '') {
        if(!cellRegEx.test(celular)) {
            return false;
        }
        return true;
    }
    return true;
}

function validarContacto(contacto){
    if(contacto != null) {
        if(contacto.value.length <4 | contacto.value.length > 50){
            return false;
        }
    
        return true;
    }
    return true;
}
    

function validarTema(tema) {
    if(tema == '0'){
        return false;
    }

    return true;
}

function validarOtro(otroTema) {
    if(otroTema != null){
        if (otroTema.value.length <3 | otroTema.value.length >15){
            return false;
        }
        return true;
    }

    return true;
}

function validarFechaInicial(fechaInicio) {
    var dateRegEx = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    if(!dateRegEx.test(fechaInicio)) {
        return false;
    }
    return true;
}

function validarFechaFinal(fechaFinal) {
    var dateRegEx = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    if(fechaFinal != '') {
        if(!dateRegEx.test(fechaFinal)) {
            return false;
        }
        return true;
    }
    
}

let contador3 = 0;

function agregarFoto(){
    let contenedor = document.getElementById('contenedorObjetos3');

    if (contador3<4){
        contador3 +=1;
        let nFoto = contador3 +1;
        contenedor.innerHTML += '<br>Foto '+ nFoto + '<br>';
        contenedor.innerHTML += '<br><input type="file" class="form-foto" name="foto-actividad" id="foto-actividad" accept="image/png, image/jpg, image/webp, image/jpeg"><br>';
    } else {
        alert("LLegó al límite de fotos");
    }
}

function validarFoto(foto) {
    if (foto == '') {
        return false;
    }
    return true;
}

let contador = 0;

function agregarWhatsapp(){
    let contenedor = document.getElementById('contenedorObjetos');
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Contacto Whatsapp: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarTelegram(){
    let contenedor = document.getElementById('contenedorObjetos');
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Contacto Telegram: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarTwitter(){
    let contenedor = document.getElementById('contenedorObjetos');
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Contacto Twitter: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarInstagram(){
    let contenedor = document.getElementById('contenedorObjetos');
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Contacto Instagram: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarFacebook(){
    let contenedor = document.getElementById('contenedorObjetos');
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Contacto Facebook: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarTiktok(){
    let contenedor = document.getElementById('contenedorObjetos')
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Contacto Tik Tok: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarOtra(){
    let contenedor = document.getElementById('contenedorObjetos');
    if (contador<5){
      contador +=1;
      contenedor.innerHTML += '<br>Otro contacto: <br>';
      contenedor.innerHTML += '<br><input type="text" class="form-contacto" name="contacto" id="contacto" minlength="4" maxlength="50"><br>';
    } else {
        alert("LLegó al límite de contactos");
    }
}

function agregarOtroTema(){
    let contador2 = 0;
    let contenedor = document.getElementById('contenedorObjetos2');

    if (contador2<1 & document.getElementById('tema').value == 'Otro'){
        contador2 +=1;
        contenedor.innerHTML += '<br>¿Cuál es su tema?<br>';
        contenedor.innerHTML += '<br><input type="text" class="form-control" name="otroTema" id="otroTema" minlength="3" maxlength="15"><br>';
    }
}