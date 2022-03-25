The Blog by Maxim Dontsov.

Do the following to run the application:

Add settings.py in blog folder. From settings.py.default ctrl+A, ctrl+V to settings.py and add SECRET KEY to settings.py

After adding info above install everything from requirements.txt file:

`pip install -r requirements.txt`

Then migrate:

`python manage.py migrate`

And runserver:

`python manage.py runserver`

On localhost: http://127.0.0.1:8000/ :
1. Create user and user profile
2. Create Category
3. Create your First Post, it will be shown on the home page

Or you can see screenshots of the Blog in the screenshots/ directory.