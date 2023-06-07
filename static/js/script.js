// Timeout function to dismiss alert messages
let messages = document.getElementById('msg');
if (messages) {
    setTimeout(() => {
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
}

// Background Animation - Add random color to squares
const borderColors = ['red', 'green', 'blue', 'yellow'];
const squares = document.querySelectorAll('.animation-square');
squares.forEach((square, i) => {
    const randColor = borderColors[Math.floor(Math.random() * borderColors.length)];
    square.classList.add(randColor);
})

// Add Custom Color And BoxShadow To Cards
const cards = document.querySelectorAll('.card');
cards.forEach((card, i) => {
    const randColor = borderColors[i % borderColors.length];
    card.classList.add(randColor);
});

// Custom Style For Blog Post Buttons
const btnColors = ['btn-red', 'btn-green', 'btn-blue', 'btn-yellow'];
const btns = document.querySelectorAll('.btn-colors')
btns.forEach((btn, i) => {
    const randBtnColors = btnColors[i % btnColors.length];
    btn.classList.add(randBtnColors);
});

// Add Current Year In Footer Section
const year = document.querySelector('#year');
year.textContent = new Date().getFullYear();

// Home Page Text Animation
// Credits to https://codepen.io/alphardex/pen/Exxodo
let textAnimations = document.querySelectorAll('.text-animation');
textAnimations.forEach(textAnimation => {
  let letters = textAnimation.textContent.split('');
  textAnimation.textContent = '';
  letters.forEach((letter, i) => {
    let span = document.createElement('span');
    span.textContent = letter;
    span.style.animationDelay = `${i * 0.1}s`;
    span.classList.add('span-animation');
    textAnimation.append(span);
  });
});

// Home Page Title Colors
// Credits to  https://stackoverflow.com/questions/65693752/how-do-i-animate-a-word-such-that-each-letter-changes-color
const titleColors = ['#e53238', '#0064d2', '#f5af02', 
'#86b817', '#e53238', '#0064d2', '#f5af02', 
'#86b817', '#e53238', '#0064d2', '#f5af02'];
let indexOffset = 0;
setInterval(() => {
  document.querySelectorAll('.span-color').forEach((letter, index) => {
    letter.style.color = titleColors[(index + indexOffset) % 11];
  })
  indexOffset++;
}, 1000)