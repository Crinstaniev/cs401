FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY model.py model.py
COPY app.py app.py
COPY model.pkl model.pkl
EXPOSE 30510
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "30510"]