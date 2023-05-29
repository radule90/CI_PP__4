// Timeout function to dismiss alert messages
setTimeout(() => {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


// Background Animation - Add random color to squares
const borderColors = ['red', 'green', 'blue', 'yellow'];
const squares = document.querySelectorAll('.animation-square');
for (let i in squares) {
    const randColor = borderColors[Math.floor(Math.random() * borderColors.length)];
    squares[i].classList.add(randColor);
}