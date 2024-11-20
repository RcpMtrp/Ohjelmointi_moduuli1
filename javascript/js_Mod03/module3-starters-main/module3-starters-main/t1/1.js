"use strict"

const newContent = `
 <li>First item</li> 
 <li>Second item</li> 
 <li>Third item</li>`

const targetElement = document.getElementById("target");
targetElement.innerHTML = newContent;
targetElement.className = "my-list";

