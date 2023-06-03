const exitNewFormBtn = document.getElementById('exitnewnote');
const exitEditFormBtn = document.getElementById('exiteditnote');

exitNewFormBtn.addEventListener('click', (exit) => {
    const confirmExit = window.confirm("There are unsaved changes are you sure you want to exit?");
    if (confirmExit == true) {
        window.location.href = '/';
    }
 });

 exitEditFormBtn.addEventListener('click', (exit) => {
    const confirmExit = window.confirm("There might be unsaved changes, are you sure you want to exit?");
    if (confirmExit == true) {
        window.location.href = '/';
    }
 });