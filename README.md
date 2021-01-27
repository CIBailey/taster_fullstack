# fullstack-exercise

## Setup database

### Requirements

In order to install database, you need to have `docker` installed on your device.

1. Clone the repository:

```bash
$ git clone https://github.com/tasterkitchens/fullstack-exercise.git
```

2. Enter the repository:

```bash
$ cd fullstack-exercise
```
3. Run docker db container:

```
$ docker run -d --name customer-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=customer -p 5432:5432 -e PGDATA=/var/lib/postgresql/data/pgdata -v $(pwd)/db-volume:/var/lib/postgresql/data postgres
```

1. Wait several seconds before running initialization script for the database to be up:

```bash
$ pip install -r scripts/requirements.txt
$ python scripts/db.py
```


5. You can now connect to the database which contains customers and orders
