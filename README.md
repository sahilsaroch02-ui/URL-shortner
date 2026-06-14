# URL Shortener

Production-quality public URL shortener API built with Python and FastAPI.

Version 1.0 is intentionally anonymous: no authentication, authorization, users,
roles, sessions, JWT, or permissions.

## Development

Install dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Configure the app:

```bash
cp .env.example .env
```

Run the API locally:

```bash
uvicorn app.main:app --reload
```

Health check:

```http
GET /health
```

## Checkpoint Status

* [x] CP-01 Bootstrap
* [x] CP-02 Configuration
* [ ] CP-03 Database
* [ ] CP-04 Migrations
* [ ] CP-05 URL Model
* [ ] CP-06 Repository
* [ ] CP-07 Short Code Generator
* [ ] CP-08 URL Validation
* [ ] CP-09 Create URL API
* [ ] CP-10 Redirect API
* [ ] CP-11 Expiration
* [ ] CP-12 Analytics
* [ ] CP-13 Security
* [ ] CP-14 Backup
* [ ] CP-15 Docker
* [ ] CP-16 Testing
* [ ] CP-17 CI/CD
