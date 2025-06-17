# 📦 Inventory Management System

A simple and scalable **CRUD API** for managing inventory items — built with **FastAPI**, **PostgreSQL**, and **Docker**.

> 🔧 Designed to showcase backend skills with clean structure, testing, and containerization.

---

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) inventory items
- ✅ RESTful API with Swagger docs (`/docs`)
- ✅ PostgreSQL database integration
- ✅ Dockerized with Compose for full dev environment
- ✅ Pytest-based API testing
- ✅ Production-ready modular structure

---

## 🧱 Tech Stack

| Layer      | Tech                |
|------------|---------------------|
| Language   | Python 3.11          |
| API        | FastAPI              |
| ORM        | SQLAlchemy           |
| Database   | PostgreSQL           |
| Testing    | Pytest + TestClient  |
| DevOps     | Docker, Docker Compose |
| Config     | python-dotenv        |

---

## 📂 Folder Structure

.
├── app/
│ ├── main.py # FastAPI app
│ ├── crud.py # DB logic
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── routes.py # API routes
│ └── database.py # DB engine/session setup
├── tests/
│ └── test_main.py # Pytest test cases
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ Getting Started

### 🛠 Prerequisites

- Docker & Docker Compose (via [Docker Desktop](https://www.docker.com/products/docker-desktop))

---

### ▶️ Run the App

```bash
# Clone the repo
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system

# Start the app (FastAPI + PostgreSQL)
`docker compose up --build`

Access the Swagger UI:
👉 http://localhost:8000/docs

### 📄 Example `.env` File
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=inventory_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

✅ Make sure this matches your docker-compose.yml

🧪 Sample API Calls (via Swagger)
POST /items – Add a new item
GET /items – List all items
PUT /items/{item_id}?quantity=8 – Update quantity
DELETE /items/{item_id} – Delete an item
🧪 Run Tests

`pytest`

Tests use FastAPI's TestClient and cover:

Create item
Get item(s)
Update item
Delete item

👤 Author
Made by
Asritha K
