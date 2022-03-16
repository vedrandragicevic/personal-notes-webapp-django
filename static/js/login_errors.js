
try {
    let myMessage = document.getElementById('vex-alert');

// myMessage.addEventListener('click', (e) => {
//     e.preventDefault();
//     console.log('Failed Login');
// });

setTimeout(() => {
    console.log("Timedout after 3 seconds");
    myMessage.style.display = 'none';
    }, 3000);
}
catch(TypeError) {
    console.log(TypeError);
}