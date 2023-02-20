dev: build run
docker: build-image push-image

build:
	/Users/crinstaniev/Documents/SPRING2023/CS401/project-2/code/venv/bin/python generate_model.py

run:
	export FLASK_APP=restapi_server.py
	export FLASK_ENV=development
	flask run --port=30510

build-image:
	docker buildx build --platform linux/amd64 --file docker/api.dockerfile --tag crinstaniev/api:v0.0.1 --tag crinstaniev/api:latest .
	docker buildx build --platform linux/amd64 --file docker/ml.dockerfile --tag crinstaniev/ml:v0.0.1 --tag crinstaniev/ml:latest .

push-image:
	docker push crinstaniev/api:v0.0.1
	docker push crinstaniev/api:latest
	docker push crinstaniev/ml:v0.0.1
	docker push crinstaniev/ml:latest

data:
	cp model.pkl shared/model.pkl
	cp data/playlist-sample-ds1.csv shared/playlist-sample-ds1.csv

forward-pods:
	kubectl port-forward service/service 30510:30510

.PHONY: data