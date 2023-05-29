# EventManger

(Work in Progress) Attempt at making a clone of Eventbrite

## Project Overview

Event Manager is a web application that allows users to manage and organize events. Users can register, log in, create events, and view events created by other users. The application provides a RESTful API for seamless integration with frontend clients.

## Table of Contents

- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Technologies Used](#technologies-used)

## Installation

To set up and install the Event Manager project, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/event-manager.git
   ```

2. Navigate to project directory:

    ```
    cd event-manager
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```
    python3 -m venv env        
    source env/bin/activate
    ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```
5. Apply database migrations:

   ```
   python manage.py migrate
   ```
6. Start the development server:

   ```
   python manage.py runserver
   ```
7. Access the application in your web browser at http://localhost:8000.

## API Documentation

The Event Manager application provides a RESTful API for managing events. Here are some key endpoints:

POST /api/auth/register/: Register a new user.
POST /api/auth/token/: Log in with username and password to obtain access and refresh tokens.
POST /api/auth/token/refresh/: Refresh an expired access token.
GET /api/events/: Retrieve a list of all events.
POST /api/events/create: Create a new event.
GET /api/events/{event_id}/: Retrieve details of a specific event.
PUT /api/events/{event_id}/: Update details of a specific event.
DELETE /api/events/{event_id}/: Delete a specific event.
Refer to the API documentation or Swagger UI for detailed information on request/response formats and authentication requirements.

## Technologies Used

The Event Manager project utilizes the following technologies:

Django: Python web framework for building the backend.
Django REST Framework: Toolkit for building RESTful APIs.
PostgreSQL: Relational database for storing event data.
React: JavaScript library for building user interfaces.
Axios: Promise-based HTTP client for making API requests.
JWT: JSON Web Tokens for authentication and authorization.
Pillow: Python Imaging Library for handling image uploads.
