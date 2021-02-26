function move() {
  var source = document.getElementById("src").value;
  var destination = document.getElementById("dst").value;
  var piece = document.getElementById(source).innerHTML;
  document.getElementById(destination).innerHTML = piece;
  document.getElementById(source).innerHTML = "&nbsp";
}
function reset() {
  location.reload();
}
