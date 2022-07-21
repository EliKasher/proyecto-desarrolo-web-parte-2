var modalBtns = document.querySelectorAll('.detalles');

modalBtns.forEach(function(btn) {
	btn.onclick = function(){
		var modal = btn.getAttribute("data-modal");

		document.getElementById(modal).style.display = "block";
	};
});

var closeBtns = document.querySelectorAll('.cerrar');

closeBtns.forEach(function(btn){
	btn.onclick = function() {
		var modal = btn.closest(".capa").style.display = 'none';
	};
});

window.onclick = function(e) {
	if(e.target.className === 'capa') {
		e.target.style.display = 'none';
	}
};