// Get the modal
var modal_nav = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    btn.classList.add("test-class");
     modal_nav.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    btn.classList.remove("test-class");
     modal_nav.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target ==  modal_nav) {
        btn.classList.remove("test-class");
         modal_nav.style.display = "none";
    }
}