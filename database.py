# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load .env file (for local testing)
load_dotenv()

# Try to read DATABASE_URL (for Render/Neon)
DATABASE_URL = os.getenv("DATABASE_URL")

# If no DATABASE_URL is found, use local database
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:aaa11123@localhost:5432/managementsys"

# Fix Neon URLs (Render sometimes needs sslmode)
if "neon.tech" in DATABASE_URL and "sslmode" not in DATABASE_URL:
    DATABASE_URL += "?sslmode=require"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
