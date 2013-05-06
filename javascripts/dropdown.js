/*Qijia (Michael) Jin*/
document.getElementById("dropdown").selectedIndex = -1;
document.getElementById("dropdown1").selectedIndex = -1;

function spoils() {
    var b0 = document.getElementById("hidden");
    var b1 = document.getElementById("button");
    if (b0.style.display == "block") {
        b0.style.display = "none";
        b1.innerHTML = "About this Project";
    } else {
        b0.style.display = "block";
        b1.innerHTML = "Hide this description";
    }
}