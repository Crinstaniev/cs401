FROM python:3.10-slim-buster
WORKDIR /app
COPY ../requirements.txt requirements.txt
COPY templates templates
COPY static static
RUN pip3 install -r requirements.txt
COPY ../model.py model.py
COPY ../app.py app.py
EXPOSE 30510
CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "30510"]