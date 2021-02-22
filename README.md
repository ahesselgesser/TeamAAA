# Team AAA
## Team member
"**Zijun Mei**" and "**Trent Wisecup**" and "**Alex Hesselgesser**"<br />

## Abstract
We will be creating a web application that users can upload Student Learning Outcome reports in pdf or word formats to. The website will process the documents and convert them into a format consistent with the database created for SLOs during a previous capstone project. The website will also perform data analysis on the data uploaded, and natural language analysis.

## Milestone 1 
For malestone 1, we simply set up the environment of developing and realized a function of file uploading. The File uploading function could allow users to upload files to the server as the first step.

## How to use the Application

First, clone the repository to your local machine:

```bash
git clone https://github.com/ahesselgesser/TeamAAA.git
```
Before running, you need to install several tools.

```bash
pip install django

pip install django-crispy-forms

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

pip install pytz
```
Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```
The application will be available at **127.0.0.1:8000**.

## Release Notes

What we doing in this milestone is to create a application that realized a function of uploading files byusing Django framework. We are Our current progress is in line with our expectations. Our next step is to wokring on parser script and database.
