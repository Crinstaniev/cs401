FROM python:3.10-slim-buster

# set working directory
WORKDIR /app

# copy requirements.txt
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy source code
COPY . .

# set environment variables 
# uncomment if use without kubernetes
# ENV REDIS_HOST=67.159.94.11
# ENV REDIS_PORT=6379
# ENV REDIS_OUTPUT_KEY=zz229-proj3-output

EXPOSE 31510

# set entrypoint
ENTRYPOINT ["python", "wsgi.py"]
