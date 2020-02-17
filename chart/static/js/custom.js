var move_flg = "";
var move_start_x = 0;
var move_start_y = 0;
// start drag
window.onmousedown = function(e) {
  move_flg = "true";
  var c = $('#obj').position();
  move_start_x = e.clientX - parseInt(c.left);
  move_start_y = e.clientY - parseInt(c.top);
}
// end drag
window.onmouseup = function(e) {
  move_flg = "false";
}
// drag
window.onmousemove = function(e) {
  if(move_flg == "true") {
    document.getElementById("obj").style.left = (e.clientX - move_start_x) + "px";
    document.getElementById("obj").style.top = (e.clientY - move_start_y) + "px";
  }
}