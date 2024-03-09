# MyDevConnect Todo List App

This repository contains the backend implementation of a todo list app developed using Flask and SQLAlchemy. The app provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on todo items. The data is persisted in a PostgreSQL database.


## Project Structure

The project structure is organized as follows:

* `app.py`: The main application file containing the Flask app configuration and API routes.
* `database`: Directory containing the database-related files.
    * `db.py`: Database connection class for PostgreSQL using SQLAlchemy.
    * `models.py`: Definition of the Todo model.
    * `data_dump.sql`: data transfered from postgresql
* venv: Virtual environment directory.

## Getting Started

Follow the steps below to set up and run the application:

1. Clone the repository:

<pre>
```
git clone https://github.com/your-username/mydevconnect-todo.git
cd mydevconnect-todo
```
</pre>

2. Create a virtual environment and activate it:
<pre>
```python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate```
```
</pre>

3. Install the required dependencies:
```pip install -r requirements.txt```

4. Configure the PostgreSQL database:
* Install PostgreSQL on your machine.
* Create a database named mydb.
* Update the database connection details in database/db.py.


5. Run the application:
```python app.py```
The app will be accessible at http://localhost:5000.

## API Endpoints

1. Create a Todo (POST)
* Endpoint: `/api/todos`

2. Get All Todos (GET)
* Endpoint: `/api/todos`

3. Get Todo by ID (GET)
* Endpoint: `/api/todos/<int:todo_id>`

4. Update Todo by ID (PUT)
* Endpoint: `/api/todos/<int:todo_id>`

5. Delete Todo by ID (DELETE)
* Endpoint: `/api/todos/<int:todo_id>`

## Export Database to SQL File

```pg_dump -h localhost -p 5432 -U username -d mydb > data_dump.sql```
Replace your_username with your PostgreSQL username.

### Contact
For any inquiries or assistance, please contact me at ofemjohn@gmail.com







