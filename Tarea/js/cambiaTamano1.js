var modalBtns = document.querySelectorAll('.i');

modalBtns.forEach(function(btn) {
	btn.onclick = function(){
		var modal = btn.getAttribute("data-modal-2");

		document.getElementById(modal).style.display = "block";
	};
});

var closeBtns = document.querySelectorAll('.c');

closeBtns.forEach(function(btn){
	btn.onclick = function() {
		var modal = btn.closest(".subcapa").style.display = 'none';
	};
});

window.onclick = function(e) {
	if(e.target.className === 'subcapa') {
		e.target.style.display = 'none';
	}
};