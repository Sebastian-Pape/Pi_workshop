function switch_light_on() {
  console.log("on");
  $.post("/light_on", {}, console.log);
}

function switch_light_off() {
  console.log("off");
  $.post("/light_off", {}, console.log);
}

function light_an() {
  console.log("on");
  $.post("/an", {}, console.log);
}

function light_aus() {
  console.log("off");
  $.post("/aus", {}, console.log);
}
