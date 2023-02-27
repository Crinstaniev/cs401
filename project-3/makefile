test:
	python -m pytest -s -v

config:
	kubectl create configmap pyfile --from-file pyfile=mymodule.py --output yaml > k8s/pyfile-config.yaml
	kubectl create configmap outputkey \
		--from-literal REDIS_OUTPUT_KEY=zz229-proj3-output \
		--output yaml > k8s/outputkey-config.yaml

clean:
	kubectl delete cm pyfile
	kubectl delete cm outputkey
	kubectl delete -f k8s/serverless-deployment-course.yaml

deploy:
	# kubectl apply -f k8s/outputkey-config.yaml 
	# kubectl apply -f k8s/pyfile-config.yaml
	# kubectl apply -f k8s/serverless-deployment-course.yaml
	kubectl apply -f k8s
	
restart: clean config deploy

requirements:
	pip freeze > requirements.txt