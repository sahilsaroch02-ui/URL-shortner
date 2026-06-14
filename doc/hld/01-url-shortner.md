# High Level Design (HLD)

## Project: URL Shortener Service

### 1. Overview

The URL Shortener Service is a backend-only application that converts long URLs into short, unique URLs. Users can access the original URL using the generated short link.

The system is designed as a production-quality practice project using Python and focuses on scalability, security, maintainability, and clean architecture principles.

---

# 2. Functional Requirements

### Core Features

#### URL Shortening

* Accept a long URL.
* Generate a unique short code.
* Store mapping in database.
* Return shortened URL.

Example:

```text
Input:
https://www.example.com/products/category/item?id=12345

Output:
https://short.ly/aB3xYz
```

---

#### URL Redirection

* User opens short URL.
* System finds original URL.
* Redirects using HTTP 301/302.

---

#### Expiration Support

* Link can have expiration date/time.
* Expired links should return:

```json
{
  "message": "Link Expired"
}
```

---

#### Analytics (Optional Production Feature)

Track:

* Total Clicks
* Last Access Time
* Creation Time

---

#### Admin APIs

* Get URL details
* Delete URL
* Disable URL

---

# 3. Non Functional Requirements

### Performance

* Redirect Response < 100 ms
* URL Creation < 200 ms

---

### Security

* HTTPS Support
* SQL Injection Protection
* JWT Authentication for Admin APIs
* Password Hashing using bcrypt
* Input Validation
* Rate Limiting

---

### Reliability

* Database Backup
* Error Logging
* Health Check Endpoint

---

### Scalability

Support:

* 10,000+ URLs
* 1,000+ requests/minute

---

# 4. Technology Stack

## Backend

* Python 3.12
* FastAPI

Why?

* High performance
* Async support
* Automatic Swagger Documentation

---

## Database

### PostgreSQL

Why?

* ACID Compliance
* Reliable indexing
* Production standard

---

## ORM

* SQLAlchemy

---

## Validation

* Pydantic

---

## Authentication

* JWT

---

## Password Hashing

* bcrypt (Passlib)

---

## Containerization

* Docker
* Docker Compose

---

## Reverse Proxy

* Nginx

---

## Caching (Future)

* Redis

---

## Monitoring

* Prometheus
* Grafana

---

# 5. High Level Architecture

```text
                +-------------+
                |   Client    |
                +------+------+
                       |
                       v

                +-------------+
                |    Nginx    |
                +------+------+
                       |
                       v

                +-------------+
                |  FastAPI    |
                +------+------+
                       |
        +--------------+--------------+
        |                             |
        v                             v

+---------------+          +----------------+
| Business      |          | Authentication |
| Logic Layer   |          | Service        |
+-------+-------+          +--------+-------+
        |                           |
        +-------------+-------------+
                      |
                      v

              +---------------+
              | SQLAlchemy ORM|
              +-------+-------+
                      |
                      v

              +---------------+
              | PostgreSQL DB |
              +---------------+
```

---

# 6. Project Structure

```text
url_shortener/

├── app/
│
├── api/
│   ├── shorten.py
│   ├── redirect.py
│   └── admin.py
│
├── services/
│   ├── shortener_service.py
│   ├── redirect_service.py
│   └── analytics_service.py
│
├── repositories/
│   └── url_repository.py
│
├── models/
│   └── url.py
│
├── schemas/
│   ├── request.py
│   └── response.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── database.py
│
├── middleware/
│   └── rate_limit.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
```

---

# 7. Database Design

### URL Table

| Column       | Type        |
| ------------ | ----------- |
| id           | UUID        |
| original_url | TEXT        |
| short_code   | VARCHAR(10) |
| created_at   | TIMESTAMP   |
| expires_at   | TIMESTAMP   |
| click_count  | INTEGER     |
| is_active    | BOOLEAN     |

---

### Admin Table

| Column        | Type      |
| ------------- | --------- |
| id            | UUID      |
| username      | VARCHAR   |
| password_hash | TEXT      |
| created_at    | TIMESTAMP |

---

# 8. API Design

## Create Short URL

```http
POST /api/v1/shorten
```

Request:

```json
{
  "url":"https://google.com",
  "expires_at":"2026-12-31"
}
```

Response:

```json
{
  "short_url":"https://short.ly/Xy12Ab"
}
```

---

## Redirect

```http
GET /{short_code}
```

Flow:

```text
Find URL
    |
Exists?
    |
   Yes
    |
Expired?
    |
 No
    |
Redirect
```

---

## Get URL Details

```http
GET /admin/url/{short_code}
```

---

## Delete URL

```http
DELETE /admin/url/{short_code}
```

---

# 9. URL Generation Strategy

### Base62 Encoding

Characters:

```text
0-9
A-Z
a-z
```

Total:

```text
62 characters
```

Example:

```text
1  -> 1
62 -> 10
125 -> 21
```

Benefits:

* Short URLs
* URL Safe
* Fast Generation

---

# 10. Security Design

### Password Storage

```text
Plain Password
      |
      v
bcrypt Hash
      |
      v
Database
```

---

### JWT Flow

```text
Login
   |
Generate JWT
   |
Return Token
   |
Protected API
   |
Verify JWT
   |
Access Granted
```

---

### Input Validation

Validate:

* URL format
* Length
* Allowed schemes

Allowed:

```text
http://
https://
```

---

# 11. Logging

Log:

* URL Created
* URL Redirected
* Login Attempts
* Errors
* Expired Access Requests

Tools:

```text
Python Logging
```

Future:

```text
ELK Stack
```

---

# 12. Production Readiness Checklist

### Core Features

* [ ] URL Shortening
* [ ] URL Redirection
* [ ] Expiration Support
* [ ] URL Validation

### Security

* [ ] JWT Authentication
* [ ] bcrypt Password Hashing
* [ ] HTTPS
* [ ] Rate Limiting
* [ ] SQL Injection Protection

### Database

* [ ] PostgreSQL
* [ ] Index on short_code
* [ ] Backup Strategy
* [ ] Migration Support (Alembic)

### DevOps

* [ ] Docker
* [ ] Docker Compose
* [ ] Environment Variables
* [ ] Health Check Endpoint

### Monitoring

* [ ] Logging
* [ ] Metrics
* [ ] Error Tracking

---

## Success Criteria

The HLD is considered implemented when:

✅ Short URL creation works
✅ Redirect works correctly
✅ Expired links are blocked
✅ PostgreSQL stores mappings safely
✅ JWT-secured admin APIs work
✅ Passwords are bcrypt hashed
✅ Docker deployment works
✅ Health check endpoint works
✅ Logging is implemented
✅ Database migrations are managed via Alembic
✅ API documentation is available via Swagger/OpenAPI
✅ Unit tests and integration tests pass (>80% coverage)

This HLD is suitable for an entry-level portfolio project while following production-grade backend architecture and coding practices.
