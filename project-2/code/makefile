dev: build run

build:
	/Users/crinstaniev/Documents/SPRING2023/CS401/project-2/code/venv/bin/python generate_model.py

run:
	export FLASK_APP=restapi_server.py
	export FLASK_ENV=development
	flask run --port=30510

build-image:
	docker build --file api.dockerfile --tag api:v0.0.1 .