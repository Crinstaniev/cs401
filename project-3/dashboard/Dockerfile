FROM python:3.10-slim-buster

# set working directory
WORKDIR /app

# copy requirements.txt
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy source code
COPY . .

EXPOSE 31510

# set entrypoint
ENTRYPOINT ["python", "app.py"]
