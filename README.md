# Crypto Data & Organization Management System

## Overview
This Django-based system allows users to manage organizations and fetch cryptocurrency prices from a public API. The system provides full CRUD APIs, scheduled updates using Celery and Redis, authentication via JWT, and additional functionalities like pagination, search, filtering, and logging.

## Features
- **Organization Management**: Create, read, update, and delete organizations.
- **Crypto Price Management**: Fetch and store live cryptocurrency prices.
- **Scheduled Updates**: Automatic price updates every 5 minutes using Celery & Redis.
- **JWT Authentication**: Secure API access using JSON Web Tokens.
- **Role-Based Permissions**: Only organization owners can edit or delete organizations.
- **Pagination & Filtering**: Implemented in crypto price API.
- **Historical Price Storage**: New prices are stored instead of being overwritten.
- **Django Signals**: Logs organization creation and deletion events.
- **Unit Tests**: Comprehensive test cases for all APIs.

## Technologies Used
- **Django** (Backend framework)
- **Django REST Framework (DRF)** (API development)
- **Simple JWT** (Authentication)
- **Celery & Redis** (Background tasks & scheduling)
- **CoinGecko API** (Fetching real-time crypto prices)
- **SQLite / PostgreSQL / MongoDB** (Database options)
- **Docker** (Optional for containerization)

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/Chintankansal48/crypto_project.git
cd crypto_project
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and add:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
CELERY_BROKER_URL=redis://localhost:6379/0
DATABASE_URL=sqlite:///db.sqlite3  # Change for PostgreSQL if needed
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

### 8. Start Redis
```bash
brew install redis  # Install Redis (Mac)
brew services start redis  # Start Redis
```

### 9. Start Celery Worker
```bash
celery -A crypto_project worker --loglevel=info
```

### 10. Start Celery Beat (For Scheduled Tasks)
```bash
celery -A crypto_project beat --loglevel=info
```

## API Endpoints
### Authentication
- `POST /api/token/` → Get JWT access & refresh tokens
- `POST /api/token/refresh/` → Refresh access token

### Organization APIs
- `GET /api/organizations/` → List all organizations
- `POST /api/organizations/` → Create an organization
- `GET /api/organizations/{id}/` → Retrieve a specific organization
- `PUT /api/organizations/{id}/` → Update an organization
- `DELETE /api/organizations/{id}/` → Delete an organization

### Crypto Price APIs
- `GET /api/crypto-prices/` → List all crypto prices (with pagination)
- `GET /api/crypto-prices/{id}/` → Retrieve a specific crypto price

## Running Tests
To run unit tests, execute:
```bash
python manage.py test
```

## Contribution
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

## License
This project is licensed under the MIT License.

