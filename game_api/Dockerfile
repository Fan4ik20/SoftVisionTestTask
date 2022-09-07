FROM python:3.10-slim-buster
WORKDIR /game_api
COPY requirements.txt /game_api/requirements.txt
RUN pip install -r /game_api/requirements.txt
COPY . /game_api
CMD ["uvicorn", "main:game_api", "--reload", "--port", "65432",  "--host", "0.0.0.0"]
