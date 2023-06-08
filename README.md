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
4. Create Note
5. Read Note
6. Edit Note
7. Delete Note
8. Browse Notes

## Views & Templates 

### Views

1. 'signin_view, signin.html' & 2. 'signup_view, signup.html'
These are the only views without the @login_required decoration.
Signin_view is the landing page, It contains a header with a H1 and a navbar with an anchor 'To Sign Up' Or 'To Sign In'. for the signup_view. Then comes the main and inside the main a div with the class "maindiv" this div is used on all views and templates but the base.html. The maindiv contains CustomAuthenticationForm or the CustomUserRegistrationForm. Input fields username & Password and a submit button. On the bottom of the page there is a footer.
Signin & Signup looks more or less the same only the forms vary and for the signup i added some JS if signup is successful to direct the user to go to the signin page. The signup_view uses ValidationErrors to communicate potential issues with the signup process. The signin simply just displays the message "Username or password incorrect." incase of unsuccessful login attempt.

#login_required on all these views below
3. base_view, base.html the main template of all the other views. This is the page a successful login redirects to. It displayas the message Welcome! When signed in successfully. There is the navbar for authenticated users. That consist of 3 anchors with images wraped inside. Add new note, browse existing notes and signout. On the bottom of the page there is the footer.

3. signout_view
If the signout icon in the navbar for authenticated users is clicked this function will redirect them to the 'signin.html' all of the views except signin and signup is decorated with @login_required.

6. note.html new_note_view by clicking the plus icon in the navbar you will be redirected to this page where you can write a new note. Title 1-50 characters, content 1-1000 characters. Each field requires atleast one character to be able to save the note by clicking the save button. There is also a exit button that if clicked user gets informed that if they exit the note has not been saved and if comfirmed redirected to the base.html.

4. browse_view browse.html if the middle a is clicked the browse view will appear. The browse view is an overview of a users notes. So inside the maindiv there is 2 more divs. one that is vertically scrollable and contains all the notes and each note is also wraped in a div. Displaying the Title as an anchor and the created_at and updated_at stamps. If you click the anchor you will you will be redirected to read.html and the specific note by its primary key. If there is no Notes yet there will only be a message stating that.

5. read.html read_view this view appears after you have saved a new note. It gets asigned a primary key and here you will see the title the note content in a scrollable div and the created at and updated at dates. There is also 3 buttons in this view, Edit to edit the note. Delete to delete and browse, to go back to the browse notes view.

8. edit.html edit_note basically looks like the add new note except the note already contains a title and content. Just like the add_note_view there is the save and the exit buttons with the same functionality. if the note has been edited and saved a success message will read update saved. If the note has not been changed a success message will state that the note is saved successfully.

7. delete.html delete_view from the read.html if the delete button/anchor is clicked you will be redirected to this view where you have to comfirm that you want to delete this note with the title of x. You will have the two options of comfirming and deleting the note or going back.

### CSS
"style.css"
Only stylesheet for the project. styling made so that everything is responsive without any media querys. Made sure there is no horizontal scrolling.

### Javascript
There are two JavaScript files.
1. "signup.js" Pre authentication JS, Listens for signup success message, if signup is successful the anchor (To Sign In) gets assigned a class that will change its appearence.

2. "script.js" To exit the add note or edit note i added a exit button. If this button is clicked, user gets a warning about potential unsaved changes and if confirmed gets redirected to dashboard (base.html).


### Models
#### User model
Djangos normal User but i made a few adjustments to the username and password requirements by editing the settings.py variable AUTH_PASSWORD_VALIDATORS & Creating the CustomUserRegistrationForm, and CustomUserAuthenticationForm.

#### Admin 
I created one superuser account for me thats the only admin.

#### Note model
Foreign key with full CRUD. In other words, Note can only be seen by the specific user that created the note and the admin. Title must contain 1-50 characthers. Note content has a length requirement of 1 - 1000 characters. The note model also has created_at and updated_at which is displayed when browsing or reading notes.


### Forms
#### 1. CustomUserRegistrationForm
##### Username & clean_username():
Username has following requirements:
3-20 character long and has to be unique. If not unique the user will get an error message stating that the username is not available. Its also given placeholder attribute of Username. If to long or to short, the user will be informed about this aswell.
##### password1 & password2. clean_password1() & clean_password2()
I set the min length to 5 in the form and in the settings.py.
The clean_password1 function gets the AUTH_PASSWORD_VALIDATORS from the settings.py file.
Incase of any errors the user will get the error messages without me having to add all the potential error messages manually. clean_password2 checks that password1 and password2 matches. If they dont, message will be displayed stating that. If they match user is registered successfully!


#### 2. CustomUserAuthenticationForm
This form requests Username and Password. It then compares the username and password to existing usernames and passwords. So either the username and password is found and user gets loged in, or the user will get an error message stating that the username or the password is in correct.


#### 3. NoteForm
This Form requests a title of 1-50 characthers and has the two meta fields title & content.

## Testing
Firstly i have manually tested everything as far as i am aware. Also there is a test.py file with three tests one for the Note model one for the CustomUserRegistrationForm and one for CustomAuthenticationForm. The test for the model was generated by chatGPT. The other two i wrote myself but parts of the code i got from chatGPT aswell. I am using it as a teacher not as an assistant for the most part. Also i was struggling to get the tests running as the project was only set up to the elephantSQL database since i followed the Django Deployment Instructions PDF as i was setting up the project. Credits to Ian_alumni in the P4 Slack Group as i used the code or atleast parts of it to access the db.sqlite3 by creating a variable in my env.py setting DEBUG as TRUE. Then uncommenting the database that came with the template and using that database if debug=true. The test for the CustomUserRegistrationForm is not covering all potential errors but i believe i have manually tested all of them. The CustomAuthenticationForm test i believe covers that whole process since there are only a few possible outcomes there. 
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
Specifically wrote the test for the Note model and i have been using it as a teacher and a tool for the most part but that specific test i just copied straight from chatGPT. Also chatGPT gave me the primarykey solution for accessing specific notes to read edit or delete them. 

[Project images from amiresponsive](https://ui.dev/amiresponsive)

[TechWithTims Youtube channel](https://www.youtube.com/@TechWithTim/featured)
[]()
[]()
[]()
[]()
