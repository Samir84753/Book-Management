### Basic RESTful web service for a book management system


The web app is on [github](https://github.com/Samir84753/Book-Management) and is built using python-django framework and drf-yasg for API documentation.

Steps to run the program:

* Create a new directory
* Open terminal or cmd on the new directory
* Run `git clone https://github.com/Samir84753/Book-Management.git` 
* Create a virtual environment using [virtualenv](https://pypi.org/project/virtualenv/). (```pip install virtualenv```)

* Activate virtual environment [for windows](https://www.codegrepper.com/code-examples/shell/how+to+activate+virtualenv+in+windows) or ``source environmentname/bin/activate`` in linux

* install requirements ``pip install -R requirements.txt``

* run `python manage.py makemigrations` and then `python manage.py migrate` to migrate database

*`python manage.py createsuperuser` to create admin account

* create .env file inside BookManagement dir and add random value to `key`. Eg key='$sse8fi=r4x6#v#q7xyvmvmc4b6rm*p='
* Then run `python manage.py runserver` to run the app.

* After that we should see ``Starting development server at http://127.0.0.1:8000/`` in the terminal


## APP

* To open admin page: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). You can login using the password you set.

* You can add or delete books from this admin page by navigating to books section.


* App API documentation link is [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

* To see and test all API [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to get list of all books

* to get book by it's isbn number `http://127.0.0.1:8000/book/{isbnnumber}`

* and also put delete and post methods can be tested from the [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api) or postman

