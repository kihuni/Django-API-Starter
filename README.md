# 🚀 Django REST API Starter Kit

A production-ready backend template with Django, DRF, JWT Auth, Docker, and CI/CD.

## Features

- 🔐 JWT Authentication (via SimpleJWT)
- 🔁 CRUD API endpoints with DRF
- 🔍 Filtering & Pagination
- 📃 OpenAPI/Swagger Documentation
- 🐳 Dockerized Setup (Django + PostgreSQL + Redis)
- 🚀 Ready to Deploy to Render/Heroku
- ✅ GitHub Actions for CI/CD

## Technologies

- Django 4.x  
- Django REST Framework  
- PostgreSQL  
- Redis (optional for caching)  
- Docker + Docker Compose  
- GitHub Actions  
- drf-spectacular (for API docs)

## Getting Started

```bash
git clone https://github.com/yourusername/drf-api-starter.git
cd drf-api-starter
cp .env.example .env
docker-compose up --build
