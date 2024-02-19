# Movies API Project

This is a movies API project where users can add a movies to a streaming platform and also review movies.

## Features

- Users can register account
- Admin can only create a streaming platform
- Users should be able to login using Token Authentication to a protected route
- Authenticated user can only perform CRUD operations on movies
- It is only a review user that can update and delete movies
- An Authenticated user can only review a movie once
- Permission classes to control access to views

## Setup

1. Clone the repository:
    ```bash
    git clone [repository-url]
    ```
2. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    python manage.py runserver 8000
    ```

7. Open the browser and go to `http://127.0.0.1:8000/`
`