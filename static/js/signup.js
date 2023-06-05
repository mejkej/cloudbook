/* If signup is successful the anchor will be asigned a class
styled in the css & chang its appearence */

window.onload = function() {
    let signupSuccess = document.getElementById('signupsuccess');
    let signinAnchor = document.querySelectorAll('.signinorupanchor');


    if (signupSuccess) {
        signinAnchor.forEach(function(a) {
            a.classList.add('ifsignupsuccessa');

        })

    }
};
