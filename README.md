This is a starting template for Melissa's IS601 project. Currently it has an
app named _notebook_ which has a single view that renders a template. A
_Notebook_ model is also defined and the view is passed all of the _Notebook_
objects via the context. Currently there are three example _Notebooks_ in the
database.

To sign in to the admin site the credentials are

* Username: melissa
* Password: melissa

To run the development server: `docker-compose up`

To make migrations: `docker-compose run web python manage.py makemigrations`

To apply migrations: `docker-compose run web python manage.py migrate`

Midterm deliverables: Create another view that uses information from the
database.
