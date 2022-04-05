# Notes Application
My personal Notes Application built using Django, HTML, CSS, Bootstrap and JS.
<br>
Steps on how to use this project:
<ol> 
    <li>
    Pull repository
    </li>
    <li>
    Install packages from 'requirements.txt file' into virtual environment
    </li>
    <li>
    Change directory to 'notesapp' and run `python manage.py runserver`
    </li>
    <li>
    If needed open .env file and edit environment variables for your own email credentials
    </li>
    <li>
    Enjoy
    </li>
</ol>
<br>This project uses sqlite DB included in the repo. API was build using django rest framework and it uses json web tokens for authentication. UI was build from scratch using Bootstrap.<br>
<hr>
<h3>Home Page</hr>
<br><br>
<p><img src="static/images/homepage.png" style="max-width: 100%;"> </p>
<hr>
<h3>TODO Notes</hr>
<br><br>
<p><img src="static/images/todonotes.png" style="max-width: 100%;"> </p>
<hr>
<h3>Completed Notes</hr>
<br><br>
<p><img src="static/images/completednotes.png" style="max-width: 100%;"> </p>
<hr>
<h3>New Note Form</hr>
<br><br>
<p><img src="static/images/noteform.png" style="max-width: 100%;"> </p>
<hr>
<h3>Single Note Edit</hr>
<br><br>
<p><img src="static/images/noteeditform.png" style="max-width: 100%;"> </p>
<hr>
<h3>Login Page</hr>
<br><br>
<p><img src="static/images/loginpage.png" style="max-width: 100%;"> </p>
<hr>
<h3>API Endpoints</h3>
<p>
        {
            'GET': '/api/notes/'
            },<br>
        {
            'GET': '/api/notes/id'
            },<br>
        {
            'GET': '/api/profiles/'
            },<br>
        {
            'POST': '/api/token/'
            },<br>
        {
            'POST': '/api/token/refresh/'
            }
    </p>