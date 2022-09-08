# Game API
## Description
Solution of a test task for the SoftVision
## Requirements
- Docker  
### Or
- Python 3.10

## Installation. First setup
- clone this repo via command  
`git clone https://github.com/Fan4ik20/SoftVisionTestTask.git`  
- ### If you want to use native Python
  - install requirements via command  
  `cd game_api && pip install -r requirements.txt`
  - Specify `.env` file in `game_api` directory   
  with this variable in the format `variable=value`
    - DB_URL
    - SECRET_KEY
## Running
- ### Via docker (app will be run on 65432 port)
  - Build images via command  
  `docker compose build`
  - Run containers in detach mode  
  `docker compose up -d`
  - To stop the containers  
  `docker compose stop`
  - To restart the containers  
  `docker compose restart`
  - To stop and remove containers  
  `docker compose down`
- ### Via Python
  - Run app via command  
  `cd game_api && uvicorn main:game_api --reload`

## Additional information
All endpoints start with `/api/v1` prefix.  
Documentation is available by this endpoint - `/api/v1/docs/`
