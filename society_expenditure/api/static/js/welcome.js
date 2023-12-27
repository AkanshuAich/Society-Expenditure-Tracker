// Get the elements from the HTML document
const logo = document.querySelector(".logo"); // The logo element
const home = document.querySelector(".active"); // The home link element
const login = document.querySelector("a[href='#login']"); // The login link element
const date = document.getElementById("date"); // The date element
const content = document.querySelector(".content"); // The content element

// Define some colors for the logo and the home link
const colors = ["#f127e6", "#f5af19", "#08aeea", "#b06ab3"];

// Define a function to change the color of the logo and the home link randomly
function changeColor() {
  // Get a random color from the colors array
  let randomColor = colors[Math.floor(Math.random() * colors.length)];
  // Set the color of the logo and the home link to the random color
  logo.style.color = randomColor;
  home.style.backgroundColor = randomColor;
}

// Add an event listener to the logo element to change the color when clicked
logo.addEventListener("click", changeColor);

// Add an event listener to the login link element to show the login form when clicked
login.addEventListener("click", showLoginForm);

// Set the date element to the current date
date.textContent = new Date().toDateString();