# Team AAA
## Team member
"**Zijun Mei**" and "**Trent Wisecup**" and "**Alex Hesselgesser**"<br />

## Abstract
We will be creating a web application that users can upload Student Learning Outcome reports in pdf or word formats to. The website will process the documents and convert them into a format consistent with the database created for SLOs during a previous capstone project. The website will also perform data analysis on the data uploaded, and natural language analysis.

<<<<<<< HEAD
## Milestone 3 
For milestone 3, we integrated a Postgresql databse into the project.
=======
## Milestone 1 
For milestone 1, we simply set up the environment of developing and realized a function of file uploading. The File uploading function could allow users to upload files to the server as the first step.
>>>>>>> d96c2b839c29a930f53b9976cf4b19c5916bd75c

## How to use the Application

First, clone the repository to your local machine:

```bash
git clone https://github.com/ahesselgesser/TeamAAA.git
```
Before running, you need to install several tools.

```bash
pip install django

pip install django-crispy-forms

python -m pip install --upgrade pip
python -m pip install --upgrade Pillow

pip install pytz
pip install psycopg2
```

Then install postgreSQL:

On Windows:
https://www.postgresql.org/download/
During installation it should ask you to set the username and password for the super user. Remember that for later.
Add your PosgreSQL bin folder to the system PATH
open PosgreSQL with:
```psql -U superusername```
and enter the password you set earlier
Now that you're in PostgreSQL the steps are the same for both linux and Windows. Please skip ahead.

On Linux:
```sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev python3-dev
```

open PosgreSQL with:
```sudo -u postgres psql```

From here the steps are the same for both:
Run the following PSQL commands in order:

```CREATE DATABASE aaadb;
CREATE USER teamaaa WITH ENCRYPTED PASSWORD 'aaapass';
ALTER ROLE teamaaa SET client_encoding TO 'utf8';
ALTER ROLE teamaaa SET default_transaction_isolation TO 'read committed';
ALTER ROLE teamaaa SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE aaadb TO teamaaa;
```

You can now exit the SQL prompt with \q

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```
The application will be available at **127.0.0.1:8000**.

Here is the video instruction of the milestone1: https://use.vg/JkjmjV
<<<<<<< HEAD
## Release Notes for Milestone 3

What we are doing in this milestone is creating an application that allows users to upload files by using the Django framework. Our current progress is in line with our expectations. Our next step is to work on integrating the parser script and database into the Django framework.

## Release Notes for Milestone 4

What we are doing in this milestone is allowing the user to view the uploaded data on the web page so they can analyze the data. Our current progress is in line with our expectations. Our next step is to work on integrating the parser script and database into the Django framework and to begin adding natural language analysis of the SLOs.


=======
## Release Notes

What we are doing in this milestone is creating an application that allows users to upload files by using the Django framework. Our current progress is in line with our expectations. Our next step is to work on integrating the parser script and database into the Django framework.
>>>>>>> d96c2b839c29a930f53b9976cf4b19c5916bd75c
