REM @echo off
REM this code follows the setting up models part of the django lecture 1.
REM to add a model, navigate to the app you want to add a model to.
REM add a class with the argument models.Model see example on next line:
REM class Question(models.Model):
REM complete the rest of the model.
REM in settings.py inside of the main project i.e. tango_with_django_project
REM if it hasn't been done, add your app (e.g. 'rango') to settings.py under
REM INSTALLED_APPS list
REM the script below is tailored for rango.

REM There is a problem with this script. To be debugged on a later date.

REM start script.
ECHO start migrateModels.bat
workon rango
python manage.py 
python manage.py makemigrations rango
python manage.py migrate
pause