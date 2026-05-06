<h1 align="center">Kosbase REST API App</h1>

This API is created by me as backend for the rent room for people in Indonesia, Kosbase app. This API use FastAPI as Python framework and MySQL as store database. [More about FastAPI](https://fastapi.tiangolo.com/)

## Built With

[![FastAPI](https://img.shields.io/badge/FastAPI-5.x-cyan.svg?style=rounded-square)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-v.3.x-yellow.svg?style=rounded-square)](https://www.python.org/downloads/)

## Requirements

1. <a href="https://www.python.org/downloads/">Python</a>
2. Web Server (ex. localhost)

## How to run the app ?

1. Open app's directory in CMD or Terminal
2. Type `python3 -m env env` for creating virtual environment (You can creating with a folder "env" name that you want)
3. Make new file a called **.env**, set up first [here](#set-up-env-file)
4. Change a content on .env file with your custom configuration like database connection.
5. Turn on Web Server and MySQL can using Third-party tool like xampp, etc.
6. Create a database with the name #nama_database, and Import file sql to **phpmyadmin**
7. You can activate python virtual environtment by type `source env/bin/activate`
8. You can install a package by type `pip install -r requirements.txt`
9. Type `uvicorn src.main:app --reload` to activated the server.
10. Open a documentation by type this link on your local server: `http://localhost:8000/docs`

## Set-up-env-file

Set up your env like this below based on your configuration :

```
DATABASE_HOST=<YOUR DATABASE HOSTNAME>
DATABASE_PORT=<YOUR DATABASE PORT>
DATABASE_USERNAME=<YOUR DATABASE USERNAME>
DATABASE_PASSWORD=<YOUR DATABASE PASSWORD>
DATABASE_NAME=<YOUR DATABASE NAME>
```

## Feature

1. Authentication
   1. Register API
   2. Login API
2. Admin Role
   1. Users API
   2. Rooms API
   3. Residents API
   4. Transactions API (Coming Soon)
   5. Payment API (Coming Soon)
3. Owner Role (Coming Soon)
4. User Role (Coming Soon)

## License

© [Muhammad Akbar Saladin Siregar](https://github.com/akbarsaladin36/)
