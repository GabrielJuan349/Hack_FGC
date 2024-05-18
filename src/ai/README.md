# My FastAPI App

This is a Python API built with FastAPI. It uses LangChain to convert text queries into SQL queries, which are then executed on a database.

## Project Structure

- `app/main.py`: Entry point of the application.
- `app/api/routes.py`: Defines the API endpoints.
- `app/models/item.py`: Defines the `Item` model.
- `app/services/langchain_service.py`: Contains `LangChainService` class.
- `app/services/database_service.py`: Contains `DatabaseService` class.
- `app/tests/test_routes.py`: Contains tests for the routes.
- `database/create_database.py`: Creates a sample database and populates it with items.

## Setup

1. Install the required Python dependencies:

```
pip install -r requirements.txt
```

## Usage

Send a POST request to `http://localhost:8000/query` with a JSON body containing a `sentence` field. The `sentence` field should contain the text you ask to the AI.


Example:

```
curl -X POST -H "Content-Type: application/json" -d '{"sentence":"Get all items"}' http://localhost:8000/query
```

The API will return the AI response.

You can poke the AI so it starts here asking.