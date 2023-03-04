.PHONY: test config clean deploy restart requirements commit

# Define variables
PYFILE = mymodule.py
REDIS_OUTPUT_KEY = zz229-proj3-output

# Dockerfile paths
DOCKERFILE_PATH_1 = dashboard
DOCKERFILE_PATH_2 = serverless-runtime

# Docker image tags
DOCKER_IMAGE_TAG_1 = crinstaniev/dashboard:latest
DOCKER_IMAGE_TAG_2 = crinstaniev/severless:latest


# Run tests
test:
	python -m pytest -s -v

# Create configmaps
config:
	kubectl create configmap pyfile --from-file pyfile=$(PYFILE) --output yaml > k8s/base/pyfile-config.yaml
	kubectl create configmap outputkey \
		--from-literal REDIS_OUTPUT_KEY=$(REDIS_OUTPUT_KEY) \
		--output yaml > k8s/base/outputkey-config.yaml

# Delete configmaps and deployment
clean:
	kubectl delete cm pyfile
	kubectl delete cm outputkey
	kubectl delete -f k8s/base/serverless-deployment-course.yaml

# Apply configmaps and deployment
deploy:
	kubectl apply -k k8s/base
	
# Restart deployment
restart: clean config deploy

# Generate requirements.txt file
requirements:
	pip freeze > requirements.txt

# Commit and push changes to git repository
commit: requirements
	@git add .
	@git commit -a 
	@git push

.PHONY: docker build-dockerfile-1 build-dockerfile-2 push-dockerfile-1 push-dockerfile-2

docker: build push

build: build-dockerfile-1 build-dockerfile-2

build-dockerfile-1:
	docker build -t $(DOCKER_IMAGE_TAG_1) $(DOCKERFILE_PATH_1)

build-dockerfile-2:
	docker build -t $(DOCKER_IMAGE_TAG_2) $(DOCKERFILE_PATH_2)

push: push-dockerfile-1 push-dockerfile-2

push-dockerfile-1:
	docker push $(DOCKER_IMAGE_TAG_1)

push-dockerfile-2:
	docker push $(DOCKER_IMAGE_TAG_2)

