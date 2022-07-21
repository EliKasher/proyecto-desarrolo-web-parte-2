
document.getElementById("formulario").addEventListener("submit", submit);
document.getElementById("ok").addEventListener("click", enviar);
document.getElementById("ko").addEventListener("click", cancelar);
 
// Funcion que se ejecuta al pulsar el botón enviar el formulario
function submit(e) {
	// Cancelams el envio a la espera de que valide el formulario
	e.preventDefault();
 
	// Mostramos la capa con el formulario de validacion
	document.getElementById("capa").style.display="block";
	document.getElementById("ok").focus();
}
 
// Funcion que se ejecuta al pulsar el boton Enviar de cuadro de dialogo
function enviar(e) {
	// Escondemos la capa
	document.getElementById("capa").style.display="none";
 
	if (validate()) {
		document.forms["formulario"].submit();
		window.location.href = "C:\Users\evely\Documents\Tarea\cgi-bin\save_data.py";
		console.log(window.location.href);
	}
	
}
 
// Funcion que se ejecuta al pulsar el boton Cancelar de cuadro de dialogo
function cancelar(e) {
	// Simplemente escondemkos el formulario
	document.getElementById("capa").style.display="none";
}