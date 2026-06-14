The implementation plan should be updated to explicitly define **v1.0 as an anonymous/public URL Shortener** with **no Authentication, Authorization, Users, Sessions, JWT, Roles, or Permissions**.

# Key Changes to the Plan

## Scope Statement

Add this section near the top of the document:

```md
# Project Scope

This project is a public URL Shortener service.

Users can create shortened URLs without creating an account.

Authentication and Authorization are intentionally excluded from v1.0 to keep the project focused on backend fundamentals, system design, database design, API development, testing, deployment, and operational practices.

Future versions may introduce user accounts and ownership models.
```

---

# Removed Features

Delete any references to:

```text
Authentication
Authorization
JWT
Refresh Tokens
User Management
Sessions
Roles
Permissions
RBAC
OAuth
Google Login
Password Hashing
Password Reset
Email Verification
```

---

# Updated Dependency Graph

```text
Project Bootstrap
        │
        ▼
Configuration
        │
        ▼
Database
        │
        ▼
Database Migrations
        │
        ▼
URL Model
        │
        ▼
Repository Layer
        │
        ▼
Short Code Generator
        │
        ▼
URL Validation
        │
        ▼
Create Short URL API
        │
        ▼
Redirect API
        │
        ▼
Expiration Engine
        │
        ▼
Analytics
        │
        ▼
Security Hardening
        │
        ▼
Backup & Recovery
        │
        ▼
Dockerization
        │
        ▼
Automated Testing
        │
        ▼
CI/CD
        │
        ▼
Release v1.0
```

---

# Updated Database Design

## urls Table

```sql
CREATE TABLE urls (
    id UUID PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP NULL,
    click_count INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);
```

Only one business table exists in v1.0.

No:

```text
users
roles
permissions
sessions
tokens
```

---

# Add New Checkpoint

The original plan is missing migrations.

Insert this checkpoint after Database.

# CP-04 Database Migrations

Branch:

```text
feature/cp-04-migrations
```

Goal:

Version control database schema.

Deliverables:

```text
Alembic setup
Initial migration
Migration scripts
```

Micro Commits:

```text
feat: configure alembic
feat: create initial migration
test: verify migration execution
feat: complete checkpoint 04 migrations
```

Test Cases:

```bash
alembic upgrade head
```

Expected:

```text
Tables created successfully
```

---

# Renumber Remaining Checkpoints

```text
CP-01 Bootstrap
CP-02 Configuration
CP-03 Database
CP-04 Migrations
CP-05 URL Model
CP-06 Repository
CP-07 Short Code Generator
CP-08 URL Validation
CP-09 Create URL API
CP-10 Redirect API
CP-11 Expiration
CP-12 Analytics
CP-13 Security
CP-14 Backup
CP-15 Docker
CP-16 Testing
CP-17 CI/CD
```

---

# Security Scope Update

Security checkpoint should focus on:

```text
Input Validation
Rate Limiting
Security Headers
Trusted Host Validation
Environment Secret Protection
SQL Injection Protection
```

Not:

```text
JWT
Token Security
Role Validation
Permission Checks
```

---

# Updated Definition of Done

## Functional

* Create short URL
* Redirect URL
* Expire URL
* Track clicks

## Reliability

* Database migrations work
* Backup and restore work

## Security

* Input validation
* SQL injection protection
* Rate limiting
* Security headers

## Quality

* Unit tests
* Integration tests
* API tests
* Coverage ≥ 80%

## Infrastructure

* Dockerized application
* GitHub Actions pipeline

## Documentation

* README
* API documentation
* Execution plan
* Setup guide

## Release

* Merged to `main`
* Tagged `v1.0.0`

---

# Final v1.0 Feature Set

✅ Shorten URL
✅ Redirect URL
✅ Expiration support
✅ Click analytics
✅ URL validation
✅ Secure code generation
✅ PostgreSQL persistence
✅ Alembic migrations
✅ Docker deployment
✅ Automated testing
✅ CI/CD pipeline
✅ Backup & recovery

❌ Authentication
❌ Authorization
❌ User accounts
❌ JWT
❌ Admin panel
❌ URL ownership
❌ Custom domains
❌ QR generation

This becomes the baseline for a clean, production-quality backend project that can realistically be completed and demonstrated in interviews while keeping the architecture extensible for a future v2.0.
