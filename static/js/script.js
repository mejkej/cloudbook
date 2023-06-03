const closeFormBtn = document.getElementById('closenewnote');

closeFormBtn.addEventListener('click', (exit) => {
    const confirmExit = window.confirm("There are unsaved changes are you sure you want to exit?");
    if (confirmExit == true) {
        window.location.href = '/';
    }
 });
