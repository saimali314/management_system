# invoTrack — FastAPI + PostgreSQL + SQLAlchemy + React

A simple full-stack demo: **FastAPI** backend with **PostgreSQL** & **SQLAlchemy**, and a **React** frontend.
- Backend runs on **http://127.0.0.1:9000**
- Frontend runs on **http://127.0.0.1:3000**

## Features (API)
- `GET /` — welcome
- `GET /products` — list all products
- `GET /products/{id}` — get one product
- `POST /products` — create product (Pydantic validation)

---

## 🧱 Project Structure
├── frontend/
│ ├── src/ # React app code
│ ├── package.json
├── myfastapi/
│ ├── Include
│ ├── Lib
│ ├── Scripts
├── database.py
├── database_model.py
├── main.py
├── model.py
└── README.md

## 🧰 Prerequisites
- Python **3.10–3.12** recommended
- OS: Windows/macOS/Linux

> **Note:** `sqlite3` is built into Python. Qt’s SQLite driver (`QSQLITE`) comes with PyQt6.

---


## 🚀 Setup & Run

### Backend
```bash
git clone https://github.com/saimali314/management_system.git
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # on Windows PowerShell
pip install -r requirements.txt
uvicorn main:app --reload --port 9000
cd frontend
npm install
npm start
```

🧰 Tech Stack
- FastAPI + Uvicorn
- SQLAlchemy + PostgreSQL 
- React (Frontend)
- Pydantic (Data validation)