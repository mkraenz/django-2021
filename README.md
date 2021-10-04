# Library Service

## FAQ

> `Import "django.blabla" could not be resolved from source Pylance`

`Ctrl Shift P` -> `Python: Select Interpreter` -> Choose the interpreter of your virtual env.

## Setup steps

Install [poetry](https://python-poetry.org/) following their guide.

```sh
poetry install
poetry run python manage.py runserver
```

### Irrelevant setup

This has been done for the initial project setup. We include it here to document a general Django project setup.

```sh
poetry new PROJECT_NAME
cd PROJECT_NAME
poetry install django
poetry install autopep8 # or black
```
