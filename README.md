# Library Service

## Getting Started

Install [poetry](https://python-poetry.org/) following their guide.

Then run,

```sh
poetry install
poetry run pre-commit install
poetry run python manage.py runserver

# optional: set this up in your terminal config once
alias ppym="poetry run python manage.py"
```

Note: If you have multiple poetry projects, you might need to activate the repository's `venv` first.

### Regular Development

```sh
# start Django dev server
poetry run python manage.py runserver

# type check
poetry run pyright

# lint (automatically executed on git commit)
poetry run black .

# coverage
poetry run coverage run --source='.' manage.py test
poetty run coverage report
```

See `launch.json` for debug configurations. Works well with VS Code.

## Deployments

```shell
# fix all problems in
manage.py check --deploy

```

## Tech Stack

- Python >=3.8
- Django - Web Framework
- [Poetry](https://www.poetryfoundation.org/) - package manager
- [Pyright](https://github.com/microsoft/pyright) - static type checking
- [Black](https://black.readthedocs.io/en/stable/index.html) - linting
- [Pre-commit](https://pre-commit.com/) - git hooks
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) - property-based testing
- Github Actions - CI
- Docker - Containerization
- [gunicorn](https://gunicorn.org/) with [gevent](http://www.gevent.org/) - wsgi compatible webserver

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

#### Deployment
poetry run gunicorn library.wsgi

# use docker-compose to run migrations
docker-compose exec web python manage.py migrate --noinput

#### Translations / i18n / i10n
# https://phrase.com/blog/posts/quick-guide-django-i18n/
mkdir MY_APP/locale
cd MY_APP
# creates a .po file in MY_APP/locale/de/LC_MESSAGES/
poetry run django-admin makemessages --locale en --locale de --locale ja
# manually translate the stuff, then
poetry run django-admin compilemessages
# manually restart dev server
# changing language header in chrome -> chrome://settings/?search=language
```

## Links

- [Awesome Django](https://github.com/wsvincent/awesome-django)
- [Django Deployment Guide](https://docs.djangoproject.com/en/3.2/howto/deployment/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/)
