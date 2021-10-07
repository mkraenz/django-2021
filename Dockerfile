FROM python:3.6-slim

ENV POETRY_VERSION=1.1.10 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

# added without assigning only for documentation
ENV SECRET_KEY \
    ALLOWED_HOSTS

WORKDIR /usr/src/app

RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock ./

# --no-dev
RUN poetry install --no-interaction --no-ansi

COPY manage.py .
COPY books ./books
COPY library ./library
COPY templates ./templates

RUN poetry run python manage.py migrate

# TODO make this work
RUN poetry run python manage.py check --deploy

EXPOSE 80
# allow connections from outside the container https://stackoverflow.com/a/60183567/3963260
CMD poetry run python manage.py runserver 0.0.0.0:80
