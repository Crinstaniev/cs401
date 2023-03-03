.PHONY: test config clean deploy restart requirements commit

# Define variables
PYFILE = mymodule.py
REDIS_OUTPUT_KEY = zz229-proj3-output

# Run tests
test:
	python -m pytest -s -v

# Create configmaps
config:
	kubectl create configmap pyfile --from-file pyfile=$(PYFILE) --output yaml > k8s/pyfile-config.yaml
	kubectl create configmap outputkey \
		--from-literal REDIS_OUTPUT_KEY=$(REDIS_OUTPUT_KEY) \
		--output yaml > k8s/outputkey-config.yaml

# Delete configmaps and deployment
clean:
	kubectl delete cm pyfile
	kubectl delete cm outputkey
	kubectl delete -f k8s/serverless-deployment-course.yaml

# Apply configmaps and deployment
deploy:
	kubectl apply -f k8s
	
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