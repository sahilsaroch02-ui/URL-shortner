# URL Shortener System Specification (SRS/SCS)

## 1. Project Overview

### Project Name

URL Shortener

### Project Type

Backend Practice Project

### Goal

Build a production-quality URL shortening service using Python while keeping the feature set intentionally small and focused.

The project should demonstrate:

* Clean Architecture
* Production-grade code quality
* API design
* Database integration
* Security best practices
* Dockerization
* Automated testing

---

# 2. Scope

## In Scope

### Core Features

1. Create Short URL
2. Redirect Short URL
3. URL Expiration
4. Click Tracking
5. URL Validation

### Engineering Features

1. Database Integration
2. Database Migrations
3. Environment Configuration
4. Logging
5. Unit Testing
6. Docker Support
7. API Documentation

---

## Out Of Scope

The following are intentionally excluded from Version 1:

* User Authentication
* User Accounts
* Custom Domains
* QR Code Generation
* Analytics Dashboard
* Redis Caching
* Database Backup Strategy
* Load Balancing
* Kubernetes
* Distributed Systems

---

# 3. Functional Requirements

## FR-1 Create Short URL

### Description

User submits a valid URL.

### Input

```json
{
  "url": "https://example.com/some/very/long/path",
  "expires_at": "2026-12-31T23:59:59Z"
}
```

### Process

1. Validate URL.
2. Generate unique short code.
3. Save record in database.
4. Return shortened URL.

### Output

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

## FR-2 Redirect URL

### Description

Redirect user from short URL to original URL.

### Process

1. Find short code.
2. Verify URL exists.
3. Verify URL is not expired.
4. Increment click count.
5. Redirect to original URL.

### Success Response

HTTP 302 Redirect

---

## FR-3 URL Expiration

### Description

Links may expire after a specified date.

### Rules

* Expired links cannot redirect.
* Expired links return error response.
* Null expiration means link never expires.

### Error Response

```json
{
  "message": "Link has expired"
}
```

---

## FR-4 Click Tracking

### Description

Track number of successful redirects.

### Rules

Increment count only after successful redirect.

---

# 4. Non-Functional Requirements

## Performance

### Target

* URL creation < 200ms
* Redirect < 100ms

---

## Reliability

### Requirements

* No duplicate short codes
* Data consistency
* Safe database transactions

---

## Maintainability

### Requirements

* Clean Architecture
* Layer separation
* Reusable services
* Dependency Injection

---

## Security

### Requirements

* URL validation
* SQL Injection protection
* Environment variables
* Centralized exception handling

---

# 5. Technology Stack

## Backend

* Python 3.12+

## API Framework

* FastAPI

## ASGI Server

* Uvicorn

## ORM

* SQLAlchemy 2.0

## Validation

* Pydantic

## Database

* PostgreSQL

## Database Migration

* Alembic

## Testing

* Pytest

## Containerization

* Docker

## Environment Management

* python-dotenv

---

# 6. Architecture

```text
Client
   |
   v
FastAPI Routes
   |
   v
Service Layer
   |
   v
Repository Layer
   |
   v
PostgreSQL
```

---

# 7. Project Structure

```text
app/
│
├── api/
│   └── routes/
│
├── services/
│
├── repositories/
│
├── models/
│
├── schemas/
│
├── core/
│   ├── config.py
│   └── database.py
│
├── tests/
│
└── main.py
```

---

# 8. Database Design

## Table: urls

| Column       | Type        |
| ------------ | ----------- |
| id           | UUID        |
| original_url | TEXT        |
| short_code   | VARCHAR(10) |
| expires_at   | TIMESTAMP   |
| click_count  | INTEGER     |
| created_at   | TIMESTAMP   |
| updated_at   | TIMESTAMP   |

---

## Indexes

### Unique Index

```sql
CREATE UNIQUE INDEX idx_short_code
ON urls(short_code);
```

### Expiration Index

```sql
CREATE INDEX idx_expires_at
ON urls(expires_at);
```

---

# 9. API Endpoints

## Create Short URL

```http
POST /api/v1/urls
```

---

## Redirect URL

```http
GET /{short_code}
```

---

## Health Check

```http
GET /health
```

---

# 10. Definition Of Done

The project is considered implemented when all items below are completed.

## URL Creation

* [ ] URL validation
* [ ] Short code generation
* [ ] Save to database
* [ ] Return short URL

---

## Redirect Flow

* [ ] Lookup short code
* [ ] Redirect works
* [ ] Click count increments
* [ ] Invalid code handled

---

## Expiration

* [ ] Expiration field stored
* [ ] Expiration checked
* [ ] Expired links blocked

---

## Database

* [x] PostgreSQL configured
* [ ] SQLAlchemy models created
* [ ] Alembic migrations created
* [ ] Database indexes created

---

## Security

* [ ] Environment variables used
* [ ] SQL injection protection
* [ ] Input validation
* [ ] Error handling

---

## Quality

* [ ] Service layer implemented
* [ ] Repository layer implemented
* [ ] Unit tests written
* [ ] Integration tests written

---

## DevOps

* [ ] Dockerfile created
* [ ] docker-compose.yml created
* [ ] Health endpoint implemented

---

## Documentation

* [ ] README completed
* [ ] API documentation available
* [ ] Architecture diagram included
* [ ] Postman collection included

---

# 11. Completion Criteria

The project is considered complete when:

* URL shortening works
* Redirect works
* Expiration works
* Click tracking works
* Database persistence works
* Docker setup works
* Tests pass
* Documentation is complete

This project intentionally focuses on backend fundamentals and production-quality engineering practices rather than advanced scalability features.
