// Timeout function to dismiss alert messages
setTimeout(() => {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);