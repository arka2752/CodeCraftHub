# CodeCraftHub API

This is the backend for the CodeCraftHub learning platform, built with Python and Flask.

## Prerequisites
- Python 3.7+
- pip (Python package installer)

## Setup and Run

1.  **Clone or navigate to the project directory**
2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate # On macOS/Linux
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python app.py
    ```
    The server will start on `http://127.0.0.1:5000`.

## API Endpoints

-   **`GET /api/courses/<id>`**: Retrieve a specific course by ID.
-   **`POST /api/courses`**: Create a new course.
    -   Requires JSON body with `title` and `instructor`.
-   **`PUT /api/courses/<id>`**: Update a course.
-   **`DELETE /api/courses/<id>`**: Delete a course.

## Troubleshooting
-   If you see "Address already in use", make sure another application is not running on port 5000.
