FROM python:3.11.4-slim-bullseye

ENV PYTHONPATH=.
ENV POETRY_VERSION=1.6.1

RUN apt update -y &&  apt install -y vim-tiny make && apt clean -y


RUN pip3 install "poetry==$POETRY_VERSION" --no-cache-dir && \
  poetry config virtualenvs.create false

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/
RUN poetry install --no-root --no-ansi

# only files explicitly configured in `.dockerignore` will be copied into the container
COPY . /usr/src/app
