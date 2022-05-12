const targetDiv = document.getElementById("third");
const btn = document.getElementById("esconder");

window.onload = esconder;
btn.onclick = function () {
    if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
    } else {
    targetDiv.style.display = "block";
    }
};