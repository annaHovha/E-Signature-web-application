# WorkShop backend
Backend application for Workshop.

A REST service on python Flask framework.

# Local development

## Requirements

- [Python 3.8](https://www.python.org/downloads/) or higher
- [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)

## Run on local machine
Create a virtualenv

```shell script
virtualenv venv
```

Activate virtualenv

```shell script 1 without sudo
sudo docker-compose up -d
```

```shell script 2
source venv/bin/activate
```
Start docker-compose services



For Database initialization

```
flask db init
```

Install  dependencies


```shell script 3, python3 -m "command"
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and change configuration to appropriate values

```shell script
cp .env.example .env
```

Run the migrations

```shell script 4 with python3 -m
flask db upgrade
```

Start the application locally

```shell script
flask run
```

## Running tests

```shell
python -m unittest discover tests
```

```shell
python -m coverage run -m unittest discover
```

```shell
python -m coverage html
```

For creating a new migration

```shell script
flask db migrate -m "migration message"
```


## Environment variables
| Variable                       | Description                                                   |
| -------------                  |:-------------:                                                |
| Some var                       | description .                                                 |


secret key = 3a1ec801-6a24-4501-b6d1-e14716b6d64f
integretion key = 6f0dcfae-db40-44a7-92fd-ed4cb8773ab9

Client ID = https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id=6f0dcfae-db40-44a7-92fd-ed4cb8773ab9&redirect_uri=http://127.0.0.1:5000/documents/code
