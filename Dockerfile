FROM python:3.13.2-alpine3.21

WORKDIR /usr/src
RUN pip install poetry
COPY pyproject.toml .env ./
COPY app/ app/
ENV PYTHONPATH /usr/src
RUN poetry install --no-root
CMD ["poetry", "run", "server"]