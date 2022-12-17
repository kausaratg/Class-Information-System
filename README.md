# Class-Information-System
A Django app for information for my Course Mate. 

# Description
<ul>
<li>Built with HTML, CSS, Python, Javascript and Django.</li>
<li>The Webapp allows users to check what group there are, It also allows the course Representative to pass important information. </li>
<li>It allows the student to download the timetable as pdf.</li>
<li>It allows the student to also comment on a post.</li>
</ul>

# Features
<ul>
<li>Signin: Allows only the Course rep to signin to be able to post information. </li>
<li>Group: Allows each member of the Department to know their group.</li>
<li>Information: Allows the student to see important information concerning the Department and allows them to comment on each post.</li>
<li>Timetable: Allows student to download the timetable as a pdf file.</li>
</ul>

## To install and run the project
1. Create a django environment 
2. clone the project             ```https://github.com/kausaratg/Class-Information-System.git``` 
3.  Enter into the directory         ```cd Class-Information-System```
4.  Pull any recent change from main branch     ```git pull origin main```
5.  create a virtual env   ```python -m venv .venv```
6. Activate the virtual env   ```source .venv/bin/activate```
7. Install dependencies  ```pip install -r requirements.txt```
8. Make migration    ```python manage.py makemigration```
9. Migrate the project   ```python manage.py migrate```
10. Run local Server  ```python manage.py runserver```
