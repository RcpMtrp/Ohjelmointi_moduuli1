"use strict"

const first = document.createElement("li")
first.textContent = "First item"

const second = document.createElement("li")
second.textContent = "Second item"
second.className = "my-item"

const third = document.createElement("li")
third.textContent = "Third item"

const targetElement = document.getElementById("target");

targetElement.appendChild(first)
targetElement.appendChild(second)
targetElement.appendChild(third)

//Open t2 folder in your IDE/editor. Add HTML by using createElement() and appenChild mehtods. (2p)
//
//     Add the following HTML code to the element with id="target"
//
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
//
//     Add class my-item to the second list item