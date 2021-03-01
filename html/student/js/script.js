let btnShow = document.querySelector('button');
let input = document.querySelector('input');

input.addEventListener('keyup', () => {
  if (input.value.length > 0) btnShow.disabled = false
  else btnShow.disabled = true;
});
