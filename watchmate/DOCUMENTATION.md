# API Documentation

This document provides documentation for a Movie REST API, which allows CRUD (Create, Read, Update, Delete) operations on Movies, Streamplatform and review movie by users.


## Setup
1. Clone this repository to your local machine:

   **git clone** [repository-url]

2. Install the requirements:

    **pip install -r requirements.txt**

3. Initialize the database and create the necessary tables:

    The database will be automatically created in an instance folder when by running the migration.

    **python manage.py makemigrations**

    After the migrations and database have been created, then you run:

    **python manage.py migrate**

4. Create a superuser:

    Create the superuser by providing the required information such as username, email, password, password2

    **python manage.py createsuperuser**

## Standand Format and Usage of Api

1. Creating a new user:
    To add a new user, send a POST request to the /account/register endpoint with a JSON payload containing the person's username, email, password and password2.

    Example:
    POST [http://127.0.0.1:8000/account/register]

    REQUEST:
    ```
    {
	"username": "John Wick",
    "email": "johnwick@email.com",
    "password": "password1234",
    "password2": "password1234"
    }
    ```
    RESPONSE:
    ```
    {
    "response": "Registration Successful!",,
    "username": "John Wick",
    "email": "johnwick@email.com",
    "token": "815efbef18792cc650a8dc49a665ec7d58994ad0"
    }
    ```
2. Log In:
    You login in using the username and password, end a POST request to the /account/login endpoint with a JSON payload containing the person's username, password.

    Example:
    POST [http://127.0.0.1:8000/account/login]

    REQUEST:
    ```
    {
	"username": "John Wick",
    "password": "password1234",
    }
    ```
    RESPONSE:
    ```
    {
    "token": "815efbef18792cc650a8dc49a665ec7d58994ad0"
    }
    ```

3. Create a streamplatform:
    To add a new streamplatform, send a POST request to the /watch/stream endpoint with a JSON payload containing the streamplatform name, about and website.

    Example:
    POST [http://127.0.0.1:8000/watch/stream]

    REQUEST:
    ```
    {
	"name": "Nexflix",
    "about": "One of the biggest movie website",
    "website": "www.nexflix.com"
    }
    ```
    RESPONSE:
    ```
    {
    "id": 1,
    "name": "Nexflix",
    "about": "One of the biggest movie website",
    "website": "www.nexflix.com"
    }

    It is only an admin that can create, delele and update a streamplatform while users can only read. And if a user tries to create, delete or update a streamplatform, it returns:

    RESPONSE:

    ```
    {
    "detail": "You do not have permission to perform this action."
    }
    ```

4. streamplatform list:
    To get a streamplatform list, send a GET request to the /watch/stream endpoint

    Example:
    GET [http://127.0.0.1:8000/watch/stream]

    RESPONSE:
    ```
    {
    "id": 1,
    "name": "Nexflix",
    "about": "One of the biggest movie website",
    "website": "www.nexflix.com"
    }

5. Retrieving a streamplatform:
    To get a streamplatform using the ID, send a GET request to the /watch/stream/<int:id> endpoint

    Example:
    GET [http://127.0.0.1:8000/watch/stream/1]

    RESPONSE:
    ```
    {
    "id": 1,
    "name": "Nexflix",
    "about": "One of the biggest movie website",
    "website": "www.nexflix.com"
    }

5. Deleating a streamplatform:
    To delete a streamplatform using the ID, send a DELETE request to the /watch/stream/<int:id> endpoint

    Example:
    DELETE [http://127.0.0.1:8000/watch/stream/1]


6. Updating a streamplatform:
    To update a new streamplatform, send a PUT request to the /watch/stream/<int:id> endpoint with a JSON payload containing the streamplatform name, about and website.

    Example:
    PUT [http://127.0.0.1:8000/watch/stream/1]

    REQUEST:
    ```
    {
	"name": "Netnaija",
    "about": "One of the biggest movie website in nigeria",
    "website": "www.netnaija.com"
    }
    ```
    RESPONSE:
    ```
    {
    "id": 1,
    "name": "Netnaija",
    "about": "One of the biggest movie website in nigeria",
    "website": "www.netnaija.com"
    }

7.  Adding a Movie:
    To add a new movie, send a POST request to the /watch/list/ endpoint with a JSON payload containing the movie's title, storyline, streamplatform and active.

    Example:
    POST [http://127.0.0.1:8000/watch/list/]

    REQUEST:
    ```
    {
	"title": "Migration",
    "storyline": "Adventure, family and animation",
    "platform": 1,
    "active": True
    }
    ```
    RESPONSE:
    ```
    {
    "id": 1,
    "title": "Migration",
    "storyline": "Adventure, family and animation",
    "platform": netflix,
    "active": True
    }

    It is only an admin that can create, delele and update a movie while users can only read. And if a user tries to create, delete or update a movie, it returns:

    RESPONSE:

    ```
    {
    "detail": "You do not have permission to perform this action."
    }
    ```

8. Movie list:
    To get a movie list, send a GET request to the /watch/list/ endpoint

    Example:
    GET [http://127.0.0.1:8000/watch/list/]

    RESPONSE:
    ```
    {
        "id": 5,
        "platform": "Nexflix",
        "title": "Hijack",
        "storyline": "Plane hijack",
        "active": true,
        "avg_rating": 4.5,
        "number_rating": 2,
        "created": "2024-01-16T09:13:36.530524Z"
    }    

9. Updating a movie:
    To update a new movie, send a PUT request to the /watch/list/<int:id> endpoint with a JSON payload containing movie title, storyline and active.

    Example:
    PUT [http://127.0.0.1:8000/watch/list/1]

    REQUEST:
    ```
    {
	    "title": "Berlin",
        "storyline": "robbery",
        "active": true,
    }
    ```
    RESPONSE:
    ```
    {
        "id": 5,
        "platform": "Nexflix",
        ""title": "Berlin",
        "storyline": "robbery",
        "active": true,
        "avg_rating": 4.5,
        "number_rating": 2,
        "created": "2024-01-16T09:13:36.530524Z"
    }

10. Retrieving a movie:
    To get a movie using the ID, send a GET request to the /watch/list/<int:id> endpoint

    Example:
    GET [http://127.0.0.1:8000/watch/list/5]

    RESPONSE:
    ```
    {
        "id": 5,
        "platform": "Nexflix",
        ""title": "Berlin",
        "storyline": "robbery",
        "active": true,
        "avg_rating": 4.5,
        "number_rating": 2,
        "created": "2024-01-16T09:13:36.530524Z"
    }

11. Deleating a movie:
    To delete a movie using the ID, send a DELETE request to the /watch/list/<int:id> endpoint

    Example:
    DELETE [http://127.0.0.1:8000/watch/list/1]

12.  Creating a Movie review:
    To add a movie review, send a POST request to the /watch/<int:pk>/review-create/ endpoint with a JSON payload containing the review's rating, description, and active.

    Example:
    POST [http://127.0.0.1:8000/watch/<int:pk>/review-create/]

    REQUEST:
    ```
    {
        "rating": 5,
        "description": "Adventure, family and animation",
        "active": True
    }
    ```
    RESPONSE:
    ```
    {
        "id": 13,
        "review_user": "Spice",
        "rating": 5,
        "description": "Adventure, family and animation",
        "active": true,
        "created": "2024-02-17T09:24:14.994137Z",
        "updated": "2024-02-17T09:24:14.994137Z"
    }

    It is only an Authenticated and review user that can create, delele and update a review while other users can only read. And if a user tries to create, delete or update a movie, it returns:

    RESPONSE:

    ```
    {
    "detail": "You do not have permission to perform this action."
    }
    ```

    A review user can only review a movie once and if a review user tries to review more than once, it returns:

    RESPONSE:

    ```
    {
    "You have already review this movie!"
    }
    ```

13. Review list:
    To get a review list, send a GET request to the /watch/<int:pk>/review/ endpoint

    Example:
    GET [http://127.0.0.1:8000/watch/5/review/]

    RESPONSE:
    ```
    {
        "id": 8,
        "review_user": "example1",
        "rating": 5,
        "description": "Great movie and thriller",
        "active": true,
        "created": "2024-01-16T14:04:58.556321Z",
        "updated": "2024-01-16T14:04:58.556321Z"
    }

14. Retrieving a review:
    To get a review using the ID, send a GET request to the /watch/review/<int:pk>/ endpoint

    Example:
    GET [http://127.0.0.1:8000/watch/review/8/]

    RESPONSE:
    ```
    {
        "id": 8,
        "review_user": "example1",
        "rating": 5,
        "description": "Great movie and thriller",
        "active": true,
        "created": "2024-01-16T14:04:58.556321Z",
        "updated": "2024-01-16T14:04:58.556321Z"
    }

15.  Updating a Movie review:
    To update a movie review, send a PUT request to the /watch/review/<int:pk>/ endpoint with a JSON payload containing the review's rating, description, and active.

    Example:
    POST [http://127.0.0.1:8000/watch/review/13/]

    REQUEST:
    ```
    {
        "rating": 5,
        "description": "Adventure, family and animation - update",
        "active": True
    }
    ```
    RESPONSE:
    ```
    {
        "id": 13,
        "review_user": "Spice",
        "rating": 5,
        "description": "Adventure, family and animation - update",
        "active": true,
        "created": "2024-02-17T09:24:14.994137Z",
        "updated": "2024-02-17T09:24:14.994137Z"
    }

11. Deleating a review:
    To delete a movie review using the ID, send a DELETE request to the /watch/review/<int:pk>/ endpoint

    Example:
    DELETE [http://127.0.0.1:8000/watch/review/1]    