window.onload = function() {
    let signupSuccess = document.getElementById('signupsuccess');
    let signinAnchor = document.querySelectorAll('.signinorupanchor');


    if (signupSuccess) {
        signinAnchor.forEach(function(a) {
            a.classList.add('ifsignupsuccessa');

        })

    }
};
