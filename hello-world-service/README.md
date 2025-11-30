# Hello World FastAPI App

A simple FastAPI application that demonstrates basic REST API functionality.

## Installation

```bash
pip install fastapi uvicorn
```

## Usage

Run the server:

```bash
uvicorn main:app --reload
```

Or with virtual environment:

```bash
& .venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

This command activates the virtual environment and runs the app on all network interfaces (`0.0.0.0`) at port 8000, allowing external connections.

The API will be available at `http://localhost:8000`

## Endpoints

- `GET /` - Returns a hello world message
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## License

MIT

## Local Execution

To run this application locally:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Start the server: `uvicorn main:app --reload`
4. Open your browser and navigate to `http://localhost:8000`
5. Access the interactive docs at `http://localhost:8000/docs`