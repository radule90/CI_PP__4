// Timeout function to dismiss alert messages
setTimeout(() => {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


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
})

// Custom Style For Blog Post Buttons
const btnColors = ['btn-red', 'btn-green', 'btn-blue', 'btn-yellow'];
const btns = document.querySelectorAll('.btn-colors')
btns.forEach((btn, i) => {
    const randBtnColors = btnColors[i % btnColors.length]
    btn.classList.add(randBtnColors);
})