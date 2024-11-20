"use strict"

const trigger = document.getElementById("trigger");
const targetImg = document.getElementById("target");

trigger.addEventListener("mouseover", function() {
    targetImg.src = "img/picB.jpg";
});

trigger.addEventListener("mouseout", function() {
    targetImg.src = "img/picA.jpg";
});
