
function addRow() {
  const div = document.createElement('div');

  div.className = 'token';
  div.innerHTML = '<input class="token-input" type="text" name="token">' +
  '<button class="sub-button" type="button" name="button" onclick="removeRow(this)">-</button>' +
  '<button class="add-button" type="button" name="button" onclick="addRow()">+</button>';
  document.getElementById('token-box').appendChild(div);
}

function removeRow(input) {
  input.parentNode.remove()
}

function showTestResults() {
  var submit = document.getElementsByClassName('submission-container')[0];
  var tests = document.getElementsByClassName('test-cases')[0];
  tests.style.display = "flex";
  submit.style.display = "none";
}

function unblockButton() {
  // const filename = document.getElementById('upload').files[0].name;
  if ( document.getElementById('upload').files.length > 0 ){
      document.getElementById("submit").style.backgroundColor = "04177E";
      document.getElementById('submit').disabled = false;
    }else{
      document.getElementById("submit").style.backgroundColor = "808080";
      document.getElementById('submit').disabled = true;
    }
}

function validate() {
  window.location.href = "student-submission.html";
}
