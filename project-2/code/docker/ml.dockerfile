FROM --platform=amd64 python:3.10-slim-buster
WORKDIR /app
COPY ../requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ../model.py model.py
COPY ../generate_model.py generate_model.py
ENV DATA_PATH=https://raw.githubusercontent.com/Crinstaniev/cs401/master/project-2/data/playlist.csv
ENV META_PATH=https://raw.githubusercontent.com/Crinstaniev/cs401/master/project-2/data/meta.json
CMD ["python3", "generate_model.py"]