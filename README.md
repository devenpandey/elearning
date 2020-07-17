# elearning
elearning Project


Setting up the e-learning project
Your final practical project will be an e-learning platform. First, create a virtual environment for your new project and activate it with the following commands:

mkdir env
python3 -m venv env/educa
source env/educa/bin/activate
Install Django in your virtual environment with the following command:

pip install "Django==3.0.*"
You are going to manage image uploads in your project, so you also need to install Pillow with the following command:

pip install Pillow==7.0.0
Create a new project using the following command:

django-admin startproject educa
Enter the new educa directory and create a new application using the following commands:

cd educa
django-admin startapp courses
Edit the settings.py file of the educa project and add courses to the INSTALLED_APPS setting, as follows:

INSTALLED_APPS = [
    'courses.apps.CoursesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
The courses application is now active for the project. Let's define the models for courses and course contents.

