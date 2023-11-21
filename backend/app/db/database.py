# Import statements for SQLAlchemy
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database connection URL
DATABASE_URL = "postgresql://david:password@db/db"


# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for SQLAlchemy models
Base = declarative_base()
