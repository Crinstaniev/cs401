dev: build run
image: build-image push-image

build:
	/Users/crinstaniev/Documents/SPRING2023/CS401/project-2/code/venv/bin/python generate_model.py

run:
	export FLASK_APP=restapi_server.py
	export FLASK_ENV=development
	flask run --port=30510

build-image:
	docker buildx build --platform linux/amd64 --file api.dockerfile --tag crinstaniev/api:v0.0.1 .
	docker buildx build --platform linux/amd64 --file ml.dockerfile --tag crinstaniev/ml:v0.0.1 .

push-image:
	docker push crinstaniev/api:v0.0.1
	docker push crinstaniev/ml:v0.0.1

delete-pods:
	kubectl delete pods --all
	kubectl delete services --all
	kubectl delete deployments --all

deploy-pods:
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml

forward-pods:
	kubectl port-forward service/recommendation-service 30510:30510