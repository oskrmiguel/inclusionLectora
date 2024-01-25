let sound = new Audio('Gotas de vida.mp3');

play_btn.addEventListener('click', ()=>{
  sound.play();
});

pause_btn.addEventListener('click', ()=>{
  sound.pause();
}); 