FROM python:3.10-slim-buster

# set working directory
WORKDIR /opt

# copy requirements.txt
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy source code
COPY . .

# set entrypoint
ENTRYPOINT ["python", "main.py"]
