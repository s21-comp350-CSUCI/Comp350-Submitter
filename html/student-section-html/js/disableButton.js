function unblockButton() {
  if ( document.getElementById('file').files.length > 0 ){
    document.getElementById('submit').disabled = false;
  }else{
    document.getElementById('submit').disabled = true;
  }
}
