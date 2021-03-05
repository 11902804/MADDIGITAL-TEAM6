# HDYFT IO Controller

# Table of Contents

1. [Dependencies](#Dependencies)
2. [Repository structure](<#Repository structure>)
3. [Database](#Database)
   1. [Connect with MySQl (remote)](<#Connect with MySQl (remote)>)
   2. [Running scripts](<#Running scripts>)
   3. [Database structure](<#Database structure>)
4. [Adding environment variables](<#Adding environment variables>)
5. [Running the app](<#Running the app>)
6. [Endpoints](#Endpoints)
7. [Testing](#Testing)
   1. [Installing PyTest](<#Installing PyTest>)
   2. [Running PyTest](<#Running PyTest>)
8. [TODO](#TODO)

# Dependencies

The project is tested and compatible with **Python 3.7**

```
$ pip3 install -r requirements.txt
```

FastAPI and uvicorn are used to run the application

```
$ pip3 install uvicorn
```

In order to connect with MySQL you should have/create a file named `.env` in your root with the following content

```
HOST="10.128.14.10"
USER="digimad"
PASSWORD="P@$$W0RD123"
DATABASE="HDYFT"
```

Always source your .env file!

```
source .env
```

Requirements are generated with pipreqs: https://pypi.org/project/pipreqs/

You don't need to use pipreqs unless you added new pip packakges to the project!

!! If you get `cannot import '__vision'` error make sure you are !!

- using Python 3.7
- Not using or having a clean conda environment
- tried `$ pip3 install mysql-connector-python `

# Repository structure

```
.
├── app
│   ├── api
│   │   ├── controllers
│   │   │   ├── color_controller.py
│   │   │   ├── emotion_controller.py
│   │   │   └── predefined_color_controller.py
│   │   └── router.py
│   ├── domain
│   │   └── models
│   │       ├── color.py
│   │       ├── emotion.py
│   │       └── predefined_color.py
│   └── infrastructure
│       └── mock
│           ├── color_repository.py
│           ├── emotion_repository.py
│           └── predefined_color_repository.py
├── main.py
├── README.md
├── requirements.txt
├── scripts
│   └── sql
│       ├── create_colors.sql
│       ├── create_emotions.sql
│       └── create_predefined_colors.sql
└── tests
    ├── test_colors.py
    └── test_sql.py
```

# Database

## Connect with MySQl (remote)

```
$ mysql -h 10.128.14.10 -u digimad -p
```

Password is P@$$W0RD123

## Running scripts

Once you have a mysql prompt make sure to use the HDYFT database

```
mysql> use HDYFT;
```

SQL scripts are located in /scripts/sql

Just copy paste them into your sql prompt

Or if you prefer to type

```
mysql> use HDYFT;
mysql> source <path_to_file>/file.sql
```

## Database structure

### Databases

#### HDYFT

```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| HDYFT              |
| information_schema |
+--------------------+
2 rows in set (0.02 sec)
```

### Tables

#### Emotions

```
mysql> desc emotions;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| id           | int          | NO   | PRI | NULL    |       |
| emotion_name | varchar(255) | NO   |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
2 rows in set (0.02 sec)

```

#### Colors

```
mysql> desc colors;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| color_name | varchar(255) | NO   | PRI | NULL    |       |
| hex_value  | varchar(255) | NO   |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```

#### Emotion color

```
mysql> desc emotion_color;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| emotion_name | varchar(255) | NO   | PRI | NULL    |       |
| nth_color    | int          | NO   | PRI | NULL    |       |
| color_name   | varchar(255) | NO   |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
```

# Adding environemnt variables

Before running the app:

1. Change credentials in .env (if you are not sure what these are, please contact Hicham)

2. run `source .env`

# Running the app

From the root folder

```
$ uvicorn main:app
```

With Swagger UI you can try out all the methods with the 'try it' button in the top right or use postman

If everything works like it should you should be able to see the changes in the HDYFT MySQL database server

An example:

```
mysql> USE HDYFT
mysql> select * from colors;
+------------+-----------+
| color_name | hex_value |
+------------+-----------+
| BLUE1      | #0000FF   |
| BLUE2      | #5900FF   |
| BLUE3      | #8576FF   |
| BROWN1     | #964B00   |
| BROWN2     | #784B00   |
| BROWN3     | #5E4B00   |
| GREEN1     | #00FF00   |
| GREEN2     | #00A900   |
| GREEN3     | #A6A900   |
| ORANGE1    | #FF7F00   |
| ORANGE2    | #CB7200   |
| ORANGE3    | #A67200   |
| PURPLE1    | #800080   |
| PURPLE2    | #8000C7   |
| PURPLE3    | #80005A   |
| RED1       | #FF0000   |
| RED2       | #BA0000   |
| RED3       | #770000   |
| YELLOW1    | #F0F000   |
| YELLOW2    | #FFC900   |
| YELLOW3    | #FFB100   |
+------------+-----------+
21 rows in set (0.00 sec)

```

# Endpoints

// TODO

// more information and structure but temp for now

| Method | Path                       | Description |
| ------ | -------------------------- | ----------- |
| GET    | /api/colors                |
| POST   | /api/colors                |
| GET    | /api/colors/{id}           |
| PUT    | /api/color/{id}            |
| DELETE | /api/colors/{id}           |
| GET    | /api/emotions              |
| POST   | /api/emotions              |
| GET    | /api/emotins/{id}          |
| PUT    | /api/emotions/{id}         |
| DELETE | /api/emotions/{id}         |
| GET    | /api/predefinedcolors      |
| POST   | /api/predefinedcolors      |
| GET    | /api/predefinedcolors/{id} |
| DELETE | /api/predefinedcolors/{id} |
| PUT    | /api/predefinedcolors      |

<br>

# Testing

## Installing PyTest

Install PyTest through pip

```
$ pip3 install pytest
```

## Running PyTest

To run all tests run the following command from the root folder

```
$ pytest
```

tests are located in /tests

Packages needed for the Lights branch:
Hypercorn
Phue
FastAPI
Pydantic
