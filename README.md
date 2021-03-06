# Team AAA
## Team member
"**Zijun Mei**" and "**Trent Wisecup**" and "**Alex Hesselgesser**"<br />

## Abstract
We will be creating a web application that users can upload Student Learning Outcome reports in pdf or word formats to. The website will process the documents and convert them into a format consistent with the database created for SLOs during a previous capstone project. The website will also perform data analysis on the data uploaded, and natural language analysis.

## Milestone 3 
For milestone 3, we integrated a Postgresql databse into the project.

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
pip install python-docx
```

Then install postgreSQL:

On Windows:

https://www.postgresql.org/download/

During installation it should ask you to set the username and password for the super user. Remember that for later.

Add your PosgreSQL bin folder to the system PATH

Open PostgreSQL with:
```psql -U postgres``` 
in the command line terminal 
and enter the password you set earlier.
If you have changed the PostgreSQL superuser name from the default, use that in place of 'postgres'.

Now that you're in PostgreSQL the steps are the same for both linux and Windows. Please skip ahead.

On Linux:
```
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev python3-dev
```

open PosgreSQL with:
```sudo -u postgres psql```

From here the steps are the same for both:
Run the following PSQL commands in order:

```
CREATE DATABASE aaadb;
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
## Release Notes for Final Milestone

The application is a document parser that you can upload select docx documents to in order to parse out the information into a database for academic assessment reports. You upload files on the upload page and can search for them on the search page. The search page has a number of filters that will help you. When you click on a link to a report you can view all of the information that was uploaded from the report.


