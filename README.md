# 🧾 Management System — FastAPI + PostgreSQL + SQLAlchemy + React

A **full-stack product management system** built using **FastAPI** (backend), **React** (frontend), and **PostgreSQL** via **SQLAlchemy ORM**.  
The project demonstrates RESTful API design, data validation with Pydantic, and modern full-stack integration.

---

## 🚀 Live Demo

- **Frontend (React on Netlify):** [https://68f6ad9bde25714da12c6e36--managementsysz.netlify.app/](https://68f6ad9bde25714da12c6e36--managementsysz.netlify.app/)
- **Backend (FastAPI on Render):** [https://management-system-5sfn.onrender.com/](https://management-system-5sfn.onrender.com/)

> 🔹 Both deployments are hosted on free tiers — please allow a few seconds for the backend to spin up when first accessed.

---

## 🧱 Tech Stack

**Frontend:**  
- React  
- Axios (API requests)  
- Bootstrap / CSS  

**Backend:**  
- FastAPI (Python 3.10+)  
- SQLAlchemy ORM  
- Pydantic (Validation)  
- PostgreSQL (Neon)  
- Uvicorn (ASGI Server)

**Deployment:**  
- Render (Backend)  
- Netlify (Frontend)  

---

## 📦 Features

✅ RESTful CRUD APIs for product management  
✅ Pydantic validation for request/response models  
✅ SQLAlchemy ORM with PostgreSQL for data persistence  
✅ CORS-enabled backend communication with React  
✅ Frontend built with React + Axios to consume APIs  
✅ Live demo deployment on Render (API) and Netlify (UI)

---

## ⚙️ Project Structure
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
- Render + Netlify