# Django_Crud_Backend

This is a simple Django backend project that provides basic CRUD (Create, Read, Update, Delete) operations for managing data using Django and SQLite. The project focuses on backend functionality only, utilizing Django’s ORM to handle database interactions and exposing API endpoints that can be tested using tools such as Postman. It demonstrates core Django concepts including models, views, URL routing, and database integration without a frontend interface.

## 📂 Project Structure

The project follows a modular Django structure where the main configuration
is separated from application logic. The `students` app handles all CRUD
operations related to student management, while the `config` directory
contains global settings and URL configurations.

``` text
django_crud_backend/
│
├── config/                  # Project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings (MySQL config)
│   ├── urls.py              # Main URL routing
│   └── wsgi.py
│
├── students/                # Student CRUD app
│   ├── migrations/          # Database migration files
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py
│   ├── models.py            # Student model
│   ├── views.py             # API CRUD logic
│   └── urls.py              # App-level API routes
│
├── manage.py                # Django command-line utility
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignored files for Git
└── README.md                # Project documentation


```
```models.py```

This file defines the structure of the database. For example, the Student model describes what information (name, email, birthday) is stored for each student. Django uses this file to understand how the database should look.

```migrations/ folder```

This folder keeps track of all changes made to the models. Whenever a model is created or updated, Django creates a migration file. These files help Django apply the correct changes to the database without losing data.

```views.py```

This file contains the backend logic. It decides what should happen when a request comes in, such as creating a student, getting student data, updating details, or deleting a record.

```urls.py```

This file connects web addresses (URLs) to views. When a request is sent from Postman or a browser, Django checks this file to know which view should handle that request.

```settings.py```

This file contains project settings such as database configuration. It connects Django to the MySQL database by storing the database name, username, and password.

How everything connects

The flow starts when a request is sent. The URL is matched in urls.py, which sends the request to a function in views.py. The view interacts with the database using the model defined in models.py. Migrations ensure the database structure matches the model, and finally, Django sends a response back to the user.

---

## 📌 Requirements

Make sure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (recommended)

---

## 🚀 Installation (First Step)

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash

git clone <your-repository-url>

cd Django_Crud_Backend
```

### 2. Create a virtual environment
```bash

python -m venv venv
````

### 3. Activate the virtual environment
```bash

venv\Scripts\activate
```

### 4. Install dependencies
```bash

pip install django
```
### 5. MySQL Database Setup
```bash

pip install mysqlclient #Install MySQL connector

```
```bash

#settings.py (connect Django ↔ MySQL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crud_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### 6. Register App
```bash

#Open config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'students',
]
```
## ▶️ Run the Server

### 1. Apply database migrations
```bash

python manage.py makemigrations
python manage.py migrate
```

### 2. Start the Django development server
```bash

python manage.py runserver
```

### 3. Open in browser
```bash

http://127.0.0.1:8000/
```
### 3. Test MySQL Connection
```bash

python manage.py shell

```
```bash

from students.models import Student
Student.objects.create(name="Test", email="test@mail.com", age=20)
Student.objects.all()

```
```bash

exit() #exit

```
### 4. Test in Postman
🟢 CREATE (POST)
Method: POST
```ruby

http://127.0.0.1:8000/api/students/

```
Body → raw → JSON
```json

{
  "name": "Kamal",
  "email": "kamal@gmail.com",
  "birthday": "2003-08-15"
}

```
Response:
```json

{
  "id": 1,
  "message": "Student created successfully"
}

```
🔵 READ (GET all)
Method: GET
```ruby

http://127.0.0.1:8000/api/students/

```
Response:
```json

[
  {
    "id": 1,
    "name": "Kamal",
    "email": "kamal@gmail.com",
    "birthday": "2003-08-15"
  }
]

```
