DOCKER_REGISTRY=docker.io
DOCKER_USERNAME=crinstaniev
IMAGE1_NAME=api
IMAGE2_NAME=ml
TAG=latest
LOG_DIR=logs

.PHONY: build-image1
build-image1:
	docker buildx build --platform linux/amd64 --file docker/api.dockerfile --tag $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE1_NAME):$(TAG) .

.PHONY: build-image2
build-image2:
	docker buildx build --platform linux/amd64 --file docker/ml.dockerfile --tag $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE2_NAME):$(TAG) .

.PHONY: push-image1
push-image1:
	docker push $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE1_NAME):$(TAG)

.PHONY: push-image2
push-image2:
	docker push $(DOCKER_REGISTRY)/$(DOCKER_USERNAME)/$(IMAGE2_NAME):$(TAG)

.PHONY: docker 
docker: build-image1 build-image2 push-image1 push-image2

.PHONY: test clear-logs
test:
	@echo "Running test..."
	@python -m pytest -s
	@echo "Test completed."

clear-logs:
	@echo "Clearing logs..."
	@for file in $(LOG_DIR)/*; do \
		echo "Deleting $$file..."; \
		rm -f $$file; \
	done
	@echo "Logs cleared."



.PHONY: push
push:
	@echo "Pushing to git..."
	# set UPDATE_TIMESTAMP to current time in format yyyy-mm-dd HH:MM:SS
	@sed -i.bak "s/UPDATE_TIMESTAMP=.*/UPDATE_TIMESTAMP=`date +"%Y-%m-%d %H:%M:%S"`/" k8s/base/config.properties
	@git add .
	@git commit -m "Update at `date +"%Y-%m-%d %H:%M:%S"`"
	@git push
	@echo "Pushed to git."



.PHONY: push-and-test
push-and-test: docker push test