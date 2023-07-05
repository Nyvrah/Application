var ambient = document.getElementById("ambient");
var light1 = document.getElementById("730nm");
var light2 = document.getElementById("850nm");
var data = document.getElementById('data');

document.getElementById("button").addEventListener("click", ()=>{eel.start()})

eel.expose(update_values)
function update_values(values){
  ambient.value = values[1];
  light1.value = values[0];
  light2.value = values[2];
  data.innerHTML = values + "<br>" + data.innerHTML;
}