# Support Ticket System

This is a simple Support Ticket System implemented using Django Rest Framework (DRF). The system allows users to raise tickets, assign them to support persons, and provide solutions.

## Features

- User and Support Person Registration
- Ticket Creation and Assignment
- Ticket Status Updates (Pending, Resolved, Closed)
- Ticket Solution Logging

### Requirements

- Python (>=3.6)
- Django
- Django REST Framework

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sahil221d/support_ticket_system.git

1. Navigate to the project directory:

    ```bash
   cd support_ticket_system

3. Create a virtual environment:
   ```bash
   python -m venv venv

5. Activate the virtual environment:
    ```bash
   For Windows: .\venv\Scripts\activate

7. Install dependencies:
   ```bash
   pip install -r requirements.txt

9. Apply database migrations:
   ```bash
   python manage.py migrate

11. Run the development server:
    ```bash
    python manage.py runserver

Your Support Ticket System should now be accessible at http://127.0.0.1:8000/.

### API Endpoints
* POST /api/add-user/: Create a new user.
* POST /api/add-support-person/: Create a new support person.
* POST /api/raise-ticket/: Raise a new ticket.
* GET /api/tickets/: Get a list of all tickets.
* GET /api/tickets/<int:pk>/: Get details of a specific ticket.
* PUT /api/tickets/<int:pk>/update/: Update a ticket with a solution.

Here are some example requests for testing the API using Postman:

1. Add Support Person
Endpoint: http://127.0.0.1:8000/api/add-support-person/
Method: POST

    Body: 
      ```bash
              {
                "username": "support_person",
                "first_name": "John",
                "last_name": "Doe",
                "email": "support@example.com",
                "phone_number": 123456789,
                "password": "support_password",
                "status": "active"
              }


2. Add User
Endpoint: http://127.0.0.1:8000/api/add-user/
Method: POST

        Body: 
         ```bash
             {
                    "username": "normal_user",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "email": "user@example.com",
                    "phone_number": 987654321,
                    "password": "user_password",
                    "status": "active"
             }



3. Raise a Ticket
Endpoint: http://127.0.0.1:8000/api/raise-ticket/
Method: POST

        Body: 
            ```bash
               {
                      "title": "Issue with the App",
                      "issue_description": "I am facing a problem with the app. Please help!",
                      "status": "pending",
                      "user": 2,
                      "support_person": 1
               }


4. Show Tickets
Endpoint: http://127.0.0.1:8000/api/tickets/
Method: GET


5. Show Ticket Details
Endpoint: http://127.0.0.1:8000/api/tickets/1/
Method: GET


6. Provide Ticket Solution
Endpoint: http://127.0.0.1:8000/api/tickets/1/update/
Method: PUT
Body:
      ```bash
      {
          "title": "Issue with the App",
          "issue_description": "I am facing a problem with the app. Please help!",
          "status": "resolved and closed",
          "user": 2,
          "support_person": 1,
          "solution": "The issue has been resolved. Please check again.",
          "solution_timestamp": "2023-12-12T12:00:00Z"
      }

7. User Access to Ticket Details
Endpoint: http://127.0.0.1:8000/api/tickets/1/
Method: GET











