# Task Management API

## Project Description
A Django REST Framework-based task management system allowing users to create, assign, and track tasks using function-based views.

## Features
- Create, read, update, and delete tasks
- Create, read, update, and delete users
- Assign tasks to multiple users
- Retrieve tasks for specific users
- Flexible task status and type tracking

## Prerequisites
- Python 3.9+
- pip
- virtualenv (recommended)

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## API Endpoints

### Tasks
- `GET /api/tasks/`: List all tasks
- `POST /api/tasks/`: Create a new task
- `GET /api/tasks/<id>/`: Retrieve a specific task
- `PUT /api/tasks/<id>/`: Update a specific task
- `DELETE /api/tasks/<id>/`: Delete a specific task
- `GET /api/tasks/user-tasks/?user_id=<id>`: Get tasks for a specific user

### Users
- `GET /api/users/`: List all users
- `POST /api/users/`: Create a new user
- `GET /api/users/<id>/`: Retrieve a specific user
- `PUT /api/users/<id>/`: Update a specific user
- `DELETE /api/users/<id>/`: Delete a specific user

## Sample Requests

### Create a Task
```json
{
    "name": "Project Documentation",
    "description": "Complete project documentation",
    "task_type": "work",
    "status": "pending",
    "assigned_user_ids": [1, 2]
}
```

### Retrieve User Tasks
Send a GET request to `/api/tasks/user-tasks/?user_id=1`

## Request and Response Examples

### Create Task
**Request:**
```http
POST /api/tasks/
Content-Type: application/json

{
    "name": "Design Backend",
    "description": "Create API endpoints",
    "task_type": "work",
    "status": "pending",
    "assigned_user_ids": [1]
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Design Backend",
    "description": "Create API endpoints",
    "created_at": "2024-03-27T10:30:45.123Z",
    "task_type": "work",
    "status": "pending",
    "assigned_users": [
        {
            "id": 1,
            "username": "johndoe",
            "email": "john@example.com"
        }
    ]
}
```

### Get User Tasks
**Request:**
```http
GET /api/tasks/user-tasks/?user_id=1
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Design Backend",
        "description": "Create API endpoints",
        "created_at": "2024-03-27T10:30:45.123Z",
        "task_type": "work",
        "status": "pending",
        "assigned_users": [
            {
                "id": 1,
                "username": "johndoe",
                "email": "john@example.com"
            }
        ]
    }
]
```






