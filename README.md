# Library Service

## Setup steps

Install [poetry](https://python-poetry.org/) following their guide.

```sh
poetry install
poetry run python manage.py runserver
poetry run pyright # type check
```

## Tech Stack

- Python >=3.6
- Django - Web Framework
- [Poetry](https://www.poetryfoundation.org/) - package manager
- [Pyright](https://github.com/microsoft/pyright) - static type checking
- [Black](https://black.readthedocs.io/en/stable/index.html) - linting
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) - property-based testing

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


#### Linting
poetry run black .
# excluding migrations
poetry run black . --exclude '^.*\b(migrations)\b.*$'

```

## Links

- [Awesome Django](https://github.com/wsvincent/awesome-django)
