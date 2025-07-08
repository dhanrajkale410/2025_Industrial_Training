// Time Clock

function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  let hours = document.getElementById("hours")
  hours.textContent = h;
  let minutes = document.getElementById("minutes")
  minutes.textContent = m;
  let seconds = document.getElementById("seconds")
  seconds.textContent = s;
  setTimeout(startTime, 1000);
}
function checkTime(i) {
  if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
  return i;
}