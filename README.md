# FullStack Exercice

## Context

The Marketing team of a food delivery company is trying to expand its customer knowledge.

To help them, the Tech team has managed to collect customer orders over the last few months and build a customer database.

The next step is now to provide an interface that allows the marketing team to see these customers...

## Objective

The aim of the exercise is to create an API to communicate with Customer Database and a Web Application which enables Marketing team to visualize company's customers.

## Assessment

The aim of the exercise is to determine ability to:

- Develop standalone and multi-tiers application:

  - API
  - Front
  - Database

- Make the application ready to be deployed:

  - Containerization usage
  - Full stack local deployment

- Develop with a high level of quality:
  - Application tests
  - Application documentation
  - Source code structure
  - Development best practices

## Expected Output

A source code repository with:

- Architecture Schema with explanations
- Documentation to run application & tests locally
- A Dockerized API, Front & Database

## Technical Requirements

### Technologies

The expected technologies are as follows :

| Resource             | Functionality      |
| -------------------- | ------------------ |
| Programming Language | Python 3.7 minimum |
| API Framework        | Flask or Fastapi   |
| Front Framework      | Vuejs / React.js   |
| Container Engine     | Docker             |
| Database             | PostgreSQL         |

### API

The Minimum API expected functionalities are the following :

| Resource | Functionality         |
| -------- | --------------------- |
| Customer | List all customers    |
| Customer | Retrieve one customer |
| Customer | Create a new customer |
| Customer | Update a customer     |
| Customer | Delete a customer     |

_Remark : API specifications and endpoints are up to you. You can add more functionalities if you need_

### Front

The Minimum expected screenrs are the following :

| Resource         | Functionality                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Customers Screen | List all company's customers                                                                     |
| Customers Screen | Filter customers by country                                                                      |
| Customers Screen | Order customers list by different dimensions (First Name, Last Name, Email, Last Orderning Date) |
| Customers Screen | Search among customers by First Name or Last Name                                                |
| Customers Screen | Display number of customers and orders split by country                                          |

_Remark : Above functionalities are the minimum required, you can add more functionalities if you want._

### Database

The database is provided to you and has the following schema :

| Table    | Functionality  | Type         | Description                     |
| -------- | -------------- | ------------ | ------------------------------- |
| Customer | uuid           | UUID4        | Customer Unique ID              |
| Customer | fist_name      | String       | Customer First Name             |
| Customer | last_name      | String       | Customer Last Name              |
| Customer | email          | String       | Customer Email                  |
| Customer | country        | String       | Customer Country (FR or UK)     |
| Customer | city           | String       | Customer City (London or Paris) |
| Order    | uuid           | UUID4        | Order Unique ID                 |
| Order    | date           | Datetime UTC | Order Date                      |
| Order    | price          | float        | Order Price                     |
| Order    | nb_or_articles | integer      | Number of article in the order  |
| Order    | shift          | String       | Meal time (Lunch or Dinner)     |

5. You can now connect to the database which contains customers and orders

## Setup

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
$ docker run -d --name customer-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=customer -p 5432:5432 -e PGDATA=/var/lib/postgresql/data/pgdata -v $(pwd)/db-volume:/var/lib/postgresql/data postgres:12
```

1. Wait several seconds before running initialization script for the database to be up:

```bash
$ pip install -r scripts/requirements.txt
$ python scripts/db.py
```
