# Library Service

## Setup steps

Install [poetry](https://python-poetry.org/) following their guide.

```sh
poetry install
poetry run python manage.py runserver
poetry run pyright # type check
```

## FAQ

### Pylance errors

VS Code shows the following error:

> `Import "django.blabla" could not be resolved from source Pylance`

Solution: `Ctrl Shift P` -> `Python: Select Interpreter` -> Choose the interpreter of your virtual env.

### Irrelevant setup

This has been done for the initial project setup. We include it here to document a general Django project setup.

```sh
poetry new PROJECT_NAME
cd PROJECT_NAME
poetry install django
poetry install autopep8 # or black
poetry run django-admin.py startproject library .
alias ppy="poetry run python"
ppy manage.py startapp books
```

### Notes

```sh
alias ppym="poetry run python manage.py"

#### Migrations
# after changing the model:
ppym makemigrations books
# inspect the sql query
ppym sqlmigrate books 0001
# apply migration
ppym migrate OPTIONAL_APP OPTIONAL_MIGRATION_NUMBER

#### Interactive shell
ppym shell



```

## Links

- [Awesome Django](https://github.com/wsvincent/awesome-django)
