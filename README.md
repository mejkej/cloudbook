![Top of home page](#)
[Link to the live project](#)
# Cloud Book.
## Introduction:
This is a web-based private note-taking application. Users can register, login, create, read, update, and delete their notes.
It is built with Django, HTML, CSS & JS. Hosted by Heroku. ElephantSQL database
and Cloudinary as static files storage. 
 
## Purpose:
Notebook accessible anywhere with the total weight of 0 grams! Currently the users notes can only be seen by the user and the admin, In the future im planing to make it so that notes can only be seen by the user, and add some encryption for the notes.
The expansion possibilitys of this project is unlimited.

## Overview of the applications functionalitys:
1. User Registration
2. Login
3. Logout
4. Created New Note
5. Read Note
6. Edit Existing Note
7. Delete Note
8. Browse All Notes

## The Frontend 
### HTML
There are 8 HTML templates.
1. signin.html
2. signup.html

3. base.html
4. browse.html
5. read.html
6. note.html
7. delete.html
8. edit.html

### CSS
"style.css"
Only stylesheet for the project. styling made so that everything is responsive without any media querys. Made sure there is no horizontal scrolling.

### Javascript
There are two JavaScript files.
1. "signup.js" Pre authentication JS, Listens for signup success message, if signup is successful the anchor (To Sign In) gets assigned a class that will change its appearence.

2. "script.js" To exit the add note or edit note i added a exit button. If this button is clicked, user gets a warning about potential unsaved changes and if confirmed gets redirected to dashboard (base.html).

## The Backend

### Models
User is djangos normal User but i just made a few adjustments to the username and password requirements by creating the CustomUserRegistrationForm, and CustomUserAuthenticationForm.

Admin i created one super user account for me thats the only admin.

The Note model. Foreign key with full CRUD. In other words, Note can only be seen by the specific user that created the note and the admin. Title must contain 1-50 characthers. Notes content only has a max length requirement of 1000 characthers.
The note model has also has created_at and updated_at which is displayed when browsing or reading notes.

### Views
1. signup_view
2. signin_view
3. signout_view
4. base_view
5. browse_notes
6. read_note
7. new_note_view
8. edit_note
9. delete_note


### Forms
CustomUserRegistrationForm

CustomUserAuthenticationForm

NoteForm


## Formating, Validating, Testing & Final Photos

## My personal thaught on the project
## Resources:

[Code Institutes template](https://github.com/Code-Institute-Org/ci-full-template)

[Background Image from Pexels](https://www.pexels.com/sv-se/foto/natur-himmel-solnedgang-moln-2114014/)

[Favicon Image from Pinterest](https://www.pinterest.se/pin/168814686018326830/)

[Background image compressed with tinypng](https://tinypng.com/)

[Favicon Converter](https://favicon.io/favicon-converter/)

[Navigation Bar Icon Images from Icons8](https://icons8.com/)
specific icon urls:
[Logout](https://icons8.com/icons/set/logout)
[Book](https://icons8.com/icons/set/book)
[Add](https://icons8.com/icons/set/add)


[Code Institutes fullstack web development course material](https://codeinstitute.net/global/)

[Geekforgeeks.org](https://www.geeksforgeeks.org/)

[chatGPT](https://openai.com/)

[]()
[]()
[]()
[]()
[]()
[]()
