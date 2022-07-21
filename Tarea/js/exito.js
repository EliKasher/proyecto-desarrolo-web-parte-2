document.getElementById("cerrar-mensaje").addEventListener("click", cerrar);
 
// Funcion que se ejecuta al pulsar el boton Cancelar de cuadro de dialogo
function cerrar() {
	// Simplemente escondemos el formulario
	document.getElementById("confirmado").style.display="none";
}