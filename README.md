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

These two templates has a different H1, Navbar and Js file than the others. They are the only pages accessible for unauthicated users. How ever the background, form container & footer is consistent to the other pages. 

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
1. signin_view
The landing page signin.html contains the CustomUserAuthenticationForm. Two fields Username & Password, 

2. signup_view
signup.html contains the CustomUserRegistrationForm. Three fields, Username, Password1 & Password2.

3. signout_view
If the signout icon in the navbar for authenticated users is clicked this function will redirect them to the 'signin.html' all of the views except signin and signup is decorated with @login_required.

4. base_view
"base.html" This in the homepage for authenticated users, and this template is used in all the views for authenticated users except for signout_view. If login was successful you will see a success message here. Also it includes a header with a h1 title and a navbar with 3 icons: Add note, browse notes and sign out.
It also contains a footer.

5. browse_notes
This view displays an overview of the users notes, title, created at & updated at date. title is an anchor tag and will take you to read.html.

6. read_note
"read.html" will display a specific note and give the user 3 options, Edit, Delete or Browse.

7. new_note_view
"note.html" If the plus icon in the navbar in the top left corner is clicked this view will appear. Containing the NoteForm with two input fields title and note content. There is also a save button that will save the note and redirect you to the read.html & a Exit button that will redirect you to 'base.html' if user confirms this since there could be usaved changes.

8. edit_note
"edit.html" pretty much the same as the add note, only this will display an existing note that you can edit. It has that same exit button as the new note view and will also redirect to read.html if save button is clicked. Once redirected the user will see a success message stating that the note has been saved either as it was before incase there has not been any changes made or updates saved.

9. delete_note
"delete.html" From read.html user has the option to delete a specific note. If button is clicked user is redirected to delete.html where user can either confirm and delete the form or go back.

### Forms
1. CustomUserRegistrationForm
#### Username
Username has following requirements:
3-20 character long and has to be unique. If not unique the user will get an error message stating that the username is not available. Its also given placeholder attribute of Username. If to long or to short, the user will be informed about this aswell.
#### Password1
Has the placeholder 'Password', I set the min length to 5 in the form and in the settings.py.
The clean_password1 function gets the AUTH_PASSWORD_VALIDATORS from the settings.py file.
Incase of any errors the user will get the error messages without me having to add all the potential error messages manually.

#### Password2
Basically checks that password1 and password2 matches if not error message will be displayed stating that.
If the match user is registered successfully!


2. CustomUserAuthenticationForm
This form basically just requests a username and a password.
It then compares the username and password to existing users.
So either the username and password is found and user gets loged in or the user will get an error message stating that the username or the password is in correct.


3. NoteForm
This form just set title length to 1-50 charachters.
added meta fields title & content.


## Formating, Validating, Testing & Final Photos

## My personal thaught on the project

## Contributing
If anyone would like to continue working on the project your welcome to!
Here is a step by step instructions to get you started.

1. Clone the repository: git clone https://github.com/mejkej/cloudbook
2. go to project directory: cd cloudbook
3. Install requirements: pip install -r requirements.txt
4. Migrate: python3 manage.py migrate
5. Run the project: python3 manage.py runserver

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

[Project images from amiresponsive](https://ui.dev/amiresponsive)

[]()
[]()
[]()
[]()
[]()
