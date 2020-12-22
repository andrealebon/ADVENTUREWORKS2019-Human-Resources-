//cancel button
var cancelButton = document.getElementById('cancel');
var cnclPopup = document.getElementById('cncl-popup');

cancelButton.addEventListener('click', function() {
  cnclPopup.classList.add('show');
  timer(cnclPopup);
});

//accept button
var acceptButton = document.getElementById('accept');
var acceptPopup = document.getElementById('accept-popup');

acceptButton.addEventListener('click',function() {
  acceptPopup.classList.add('show');
  timer(acceptPopup);
});

function timer(element) {
  setTimeout(function(){
  element.classList.remove('show');
  }, 8000);
}