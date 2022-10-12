var modal1 = document.getElementById("myModal1");
var modal2 = document.getElementById("myModal2");
// Get the button that opens the modal
var btn = document.getElementById("myBtn");
var temperature = document.getElementById("Temperature")
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var age = document.getElementById("Age");

// When the user clicks on the button, open the modal
btn.onclick = function() {
  if(age.value > 50){ 
  //console.log(age)
  modal1.style.display = "block";
  }
  else if (temperature.value > 37 ){
    modal2.style.display ="block"
  }
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
  else if(event.target == modal2){
    modal2.style.display = "none";
  }
}
