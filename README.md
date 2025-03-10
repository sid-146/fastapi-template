[![Python Linting](https://github.com/sid-146/fastapi-template/actions/workflows/fastapi-pylint.yml/badge.svg)](https://github.com/sid-146/fastapi-template/actions/workflows/fastapi-pylint.yml)

# FastAPI Template Repository

This repository provides a fast and easy starting point for building RESTful APIs with [FastAPI](https://fastapi.tiangolo.com/). It includes a minimal, yet comprehensive setup to get you up and running quickly, with sensible defaults for projects of any size.

## Features

-   **FastAPI**: Fast and modern web framework for building APIs with Python 3.7+.
-   **SQLAlchemy**: ORM for interacting with databases.
-   **Alembic**: For database migrations.
-   **Pydantic**: For data validation and serialization.
-   **Docker**: Containerization setup for easy deployment.
-   **Testing**: Setup for unit tests and integration tests.
-   **Pre-configured CORS**: Easily configurable for cross-origin requests.
-   **Environment configuration**: Manage environment variables with `.env` files.
-   **Swagger UI**: Automatic generation of API documentation.

## Getting Started

### Prerequisites

Make sure you have the following tools installed:

-   Python 3.8 (preferably 3.9 or higher)
-   [Docker](https://www.docker.com/)
-   [Poetry](https://python-poetry.org/) (optional, for dependency management)

### Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/sid-146/fastapi-template.git
cd fastapi-template
```

### Create Virtual Env

Using python `venv` module create a virtual environment

```bash
python -m venv venv
```

or

```bash
py -m venv venv
```

### Activate Virtual Env

Navigate to Scripts in virtual environment.

```bash
cd venv/Scripts
```

run `activate` script. After this your environment will be activated.

### Install Dependencies

Using `pip` (for standard Python environments):

```bash
pip install -r requirements.txt
```

Or using `Poetry`:

```bash
poetry install
```

### Configure Environment Variables

Copy the example environment file and edit the values as necessary:

```bash
cp .env.example .env
```

Make sure to update your `.env` file with the appropriate settings for your local environment (e.g., database URL, secret keys).

### Run the Application

To run the application, you can use the following command:

```bash
uvicorn app.main:app --reload
```

Or Run using `app.py` file

```bash
cd src
py app.py
```

This will start the FastAPI server at `http://localhost:8000`.

### Docker Setup (Optional)

If you prefer using Docker to run the application, you can build and start a container using:

```bash
docker-compose up --build
```

Once the container is up, the app will be accessible at `http://localhost:8000`.

## Project Structure

```plaintext
fastapi-template/
├── src/
│   ├── app.py                      # FastAPI application instance
│   ├── models/                     # Database models
├── ├── api/
├── ├──  ├──  __init__.py           # Holds all the routers created in routes folder
├── ├──  ├──  routes/               # Routes of different endpoint
├── ├──  ├──  middleware/           # Middleware required
├── ├──  ├──  models/               # Models for request and respones
├── ├──  ├──   ├── requests/        # Requests models
├── ├──  ├──   ├── responses/       # Responses models
├── ├──  ├──  functions/            # Business Logic Functions
├── ├── components/
├── ├── core/                       # Core config like server starting config
├── ├──  ├── config.py              # Config flie
├── ├── db/
├── ├──  ├── models/                # DB Models
├── ├──  ├── scripts/               # DB Scripts
├── ├── utils/
├── ├── test/
├── alembic/                        # Database migrations
├── .env.example                    # Example environment configuration file
├── Dockerfile                      # Dockerfile for containerizing the app (todo)
├── docker-compose.yml              # Docker Compose configuration (todo)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Testing

To run tests, use the following command:

```bash
pytest
```

Make sure that your test cases are properly configured in the `tests/` folder.

## Deployment

This template is ready for deployment with Docker and can be deployed on any platform that supports Docker (e.g., AWS, Heroku, DigitalOcean).

You can also deploy directly to a cloud service like [Uvicorn with Gunicorn](https://www.uvicorn.org/) for better production performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## To use this

Feel free to customize this as needed by forking this repository 🍴!
