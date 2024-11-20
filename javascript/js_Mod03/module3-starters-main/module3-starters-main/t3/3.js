'use strict';
const names = ['John', 'Paul', 'Jones'];
const targetElement = document.getElementById("target");

for (let i =0; i<names.length; i++) {
  const newLi = document.createElement("li");
  newLi.textContent = names[i];
  targetElement.appendChild(newLi);
}

