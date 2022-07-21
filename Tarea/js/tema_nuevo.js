function tema_nuevo(){
    let contenedor = document.getElementById('contenedorOpciones');

    if (document.getElementById('tema').value == 'Otro'){
        var otro = document.getElementById('otroTema').value;
        contenedor.innerHTML += ' <option value=" ' + otro + ' "> ' + otro + ' </option> ';
    }
}