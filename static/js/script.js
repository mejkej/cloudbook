const exitNewFormBtn = document.getElementById('exitnewnote');


exitNewFormBtn.addEventListener('click', (exit) => {
    var confirmExit = window.confirm("Note has not been saved. Are you sure you want to exit?");
    if (confirmExit == true) {
        window.location.href = '/';
    }
 });