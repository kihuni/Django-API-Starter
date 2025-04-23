# Django API Starter

A production-ready Django REST API template with JWT authentication and Swagger/ReDoc documentation.

## Features
- JWT Authentication (register, login, token refresh)
- REST API with sample Profile CRUD endpoints
- Auto-generated Swagger/ReDoc API docs
- PostgreSQL + Docker setup
- Pytest for testing

## Setup
1. Clone the repo: `git clone <repo-url>`
2. Install Docker and Python 3.11
3. Copy `.env.example` to `.env` and update variables
4. Run: `docker-compose -f docker/docker-compose.yml up`
5. Access Swagger at `http://localhost:8000/swagger/`

## Endpoints
- `POST /api/users/register/` - Register a user
- `POST /api/users/login/` - Login and get tokens
- `GET /api/profiles/` - List user profiles (authenticated)

## License
MIT License