var modal = document.getElementById("modal-app-preview");

var btn = document.getElementsByName("app-preview");
for (var i = 0; i < btn.length; i++) {
    btn[i].addEventListener('click', function() {
      modal.style.display = "block";
    }, false);
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
