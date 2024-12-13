# DevOps Learning REST API

## Project Overview
This is a simple REST API project built with FastAPI.

## Features
- CRUD operations for Items
- Containerized with Docker
- Pytest for automated testing
- Simple, extensible design

## Prerequisites
- Python 3.9+
- Docker (optional)
- pip

## Local Setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Running with Docker
```bash
docker build -t devops-rest-api .
docker run -p 8000:8000 devops-rest-api
```

## API Endpoints
- `POST /items/`: Create a new item
- `GET /items/`: List all items
- `GET /items/{item_id}`: Retrieve a specific item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

