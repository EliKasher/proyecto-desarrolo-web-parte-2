document.getElementById('tema').onclick = function(){
    let contenedor = document.getElementById('contenedorObjetos2');
    
    if (document.getElementById('tema').value != 'Otro'){
        contenedor.innerHTML = '';
    }
}