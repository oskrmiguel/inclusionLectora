let audio = document.querySelector('.mus');
let play = document.querySelector('.play');
let pause = document.querySelector('.pause');

let fast = document.querySelector('.forward');
let slow = document.querySelector('.backward');

let playrate = document.querySelector('.playrate');

let songUrl = "/audio.mp3";

let backw = document.querySelector('.backw');
let forw = document.querySelector('.forw');


play.addEventListener('click', function (e) {
  play.style.display = 'none';
  pause.style.display = 'inline-block';
  audio.play();
});

pause.addEventListener('click', function () {
  pause.style.display = 'none';
  play.style.display = 'inline-block';
  audio.pause();
});

info.addEventListener('click', function () {
  console.log(`${Math.floor(audio.duration / 60)}:${Math.floor(audio.duration % 60)}`);
});

fast.addEventListener('click', function () {
  audio.playbackRate += 0.25;
});

slow.addEventListener('click', function () {
  audio.playbackRate -= 0.25;
});

backw.addEventListener('click', function () {
  audio.currentTime -= 5;
});

forw.addEventListener('click', function () {
  audio.currentTime += 5;
});

setInterval(function() {
  playrate.innerHTML = `${Math.floor(audio.currentTime / 600)}${Math.floor((audio.currentTime / 60) % 10)}:${Math.floor((audio.currentTime / 10)%6)}${Math.floor(audio.currentTime % 10)}`;
}, 1000);

audio.src = songUrl;
