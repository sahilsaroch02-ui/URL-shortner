# CLAUDE.md

## Project

Production-quality URL Shortener built with:

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Docker
* Pytest
* GitHub Actions

No Authentication or Authorization in v1.0.

---

## Development Process

Follow Checkpoint Driven Development.

Rules:

* Never commit to `main`
* Never commit to `develop`
* One checkpoint = one feature branch
* Complete and test a checkpoint before starting the next
* Use micro commits
* Push frequently
* Merge only after tests pass
* Delete feature branch after merge

---

## Git Workflow

Start every checkpoint:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/cp-XX-name
```

Work using micro commits:

```bash
git add .
git commit -m "feat: description"
git push origin feature/cp-XX-name
```

Final checkpoint commit:

```bash
git commit -m "feat: complete checkpoint XX"
```

Merge:

```bash
git checkout develop
git merge feature/cp-XX-name
git push origin develop
```

Delete branch:

```bash
git branch -d feature/cp-XX-name
git push origin --delete feature/cp-XX-name
```

---

## Commit Convention

```text
feat:
fix:
refactor:
test:
docs:
chore:
```

Examples:

```text
feat: add url repository
test: add repository tests
docs: update readme
chore: configure alembic
```

---

## Checkpoint Order

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

Never skip checkpoint dependencies.

---

## Testing Requirement

Every checkpoint must:

* Have test cases
* Pass all tests
* Update documentation
* Be merged into develop

Checkpoint is complete only after merge.

---

## Definition of Done

* URL shortening works
* URL redirect works
* Expiration works
* Analytics works
* Security checks pass
* Docker works
* Tests pass
* CI/CD passes
* Documentation updated
* Release ready
