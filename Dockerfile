FROM python:3.10-slim

# all of this is required for poetry
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# set the working directory to some known place inside the container
WORKDIR /app

# copy the dependency specifications over
COPY pyproject.toml poetry.lock* ./

# install the dependencies, disable virtual envs because the container
# is the virtual env now
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# copy the app
COPY . .

# expose the port that we want to use
EXPOSE 6080

# run the gunicorn application so that it's nice and production ready
CMD ["gunicorn", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:6080", "--access-logfile", "-", "main:app"]
