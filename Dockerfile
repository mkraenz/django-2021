FROM python:3.9-slim as builder

ENV POETRY_VERSION=1.1.10 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=true

# added without assigning only for documentation
ENV SECRET_KEY \
    ALLOWED_HOSTS

WORKDIR /usr/src/app

RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-interaction --no-ansi

RUN poetry export --format requirements.txt --output requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

COPY manage.py .
COPY books ./books
COPY library ./library
COPY templates ./templates
COPY py_library_service ./py_library_service
COPY utils ./utils

# TODO how to handle migrations in production?
# RUN python manage.py migrate

# TODO make this work
RUN poetry run python manage.py check --deploy

# allow connections from outside the container https://stackoverflow.com/a/60183567/3963260
# CMD poetry run gunicorn --bind 0.0.0.0:80 --worker-class gevent --access-logfile - --error-logfile - --workers $GUNICORN_WORKERS library.wsgi

################################################################################
# Production
################################################################################
# Following https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

FROM python:3.9-slim as prod

ARG GUNICORN_WORKERS=2
ENV GUNICORN_WORKERS=$GUNICORN_WORKERS

# todo consider rename of user and group to django
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $HOME
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN addgroup --system app && adduser --system app && adduser app app

COPY entrypoint.prod.sh .
COPY --from=builder /usr/src/app .
RUN pip install --no-cache ./wheels/*
RUN rm -rf ./wheels

RUN chown -R app:app $APP_HOME

USER app
# NOTE: currently this creates a sqlite db in $APP_HOME. To give app user write permissions, call this command as app user
# TODO: Probably dont run migrations during build?
# RUN python manage.py migrate

EXPOSE 80
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
