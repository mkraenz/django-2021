FROM python:3.9-slim as builder

ARG GUNICORN_WORKERS=2
ENV GUNICORN_WORKERS=$GUNICORN_WORKERS

ENV POETRY_VERSION=1.1.10 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

# added without assigning only for documentation
ENV SECRET_KEY \
    ALLOWED_HOSTS

WORKDIR /usr/src/app

RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-interaction --no-ansi
RUN rm -rf /root/.cache

COPY manage.py .
COPY books ./books
COPY library ./library
COPY templates ./templates
COPY utils ./utils

RUN python manage.py migrate

# TODO make this work
RUN python manage.py check --deploy

EXPOSE 80
# allow connections from outside the container https://stackoverflow.com/a/60183567/3963260
CMD gunicorn --bind 0.0.0.0:80 --worker-class gevent --access-logfile - --error-logfile - --workers $GUNICORN_WORKERS library.wsgi
