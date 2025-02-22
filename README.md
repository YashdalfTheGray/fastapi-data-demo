# fastapi-data-demo

Building a demo with FastAPI and a dummy data class

## API

### `GET /`

Redirects to `/api/v1`

### `GET /api/v1`

Provides a bit of sass and a status

### `GET /api/v1/ping`

Provides just the status, no sass

### `GET /api/v1/nodes`

Returns the list of nodes kwown to the graph

### `GET /api/v1/nodes/<node_id>`

Returns the information the graph has on a particular node

### `GET /api/v1/nodes/<node_id>/neighbors`

Returns all the neighbors of a particular node

## testing

First and foremost, poetry has to activate the virtual environment, otherwise, nothing will work.

The command for it used to be `poetry shell` but that's been moved to a different plugin and we hate that. So instead, activating the virtual environment now has to happen via

```
eval $(poetry env activate)
```

Once that's done, we can run

```
uvicorn main:app --host 0.0.0.0 --port 6080 --reload
```

Uvicorn will also reload after changes are made to the server. This is nice, and the color logs are good too.

If we want to run this in a more production ready way, we can use gunicorn with uvicorn workers to spin up several threads that will all respond to the endpoints. The `--access-logfile -` redirects the gunicorn logs to stdout. Note that uvicorn's logging system is 100034340 times better than gunicorn's trash but gunicorn is a bit better for production usecases.

```
gunicorn --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:6080 --access-logfile - main:app
```

To exit the virtual environement once we're happy, use `deactivate`.

## testing with docker

Docker's even simpler and we don't need any of this virtual evironment garbage. Just run

```
docker build -t fastapi-data-demo .
```

to build the docker image that has already been programmed to use gunicorn and output logs to stdout.

Then run

```
docker run -it --rm -p 6080:6080 --name fastapi-instance fastapi-data-demo:latest
```

to start a new docker container that is hosting the API. You can check logs by running

```
docker logs -f fastapi-instance
```
