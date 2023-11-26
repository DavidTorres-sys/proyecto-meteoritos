from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.crud.tables_data import get_tables_have_data
from app.utils.initialization import init_data_on_startup
from app.utils.database import get_db, logger  
from app.db.database import SessionLocal, engine
from app.api.endpoints import earthquake, user
from app.domain import models

# Create tables if they do not exist
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app instance
app = FastAPI()

# Define the list of allowed origins
origins = [
    "http://localhost",
    "http://localhost:4200",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

# Dependency to get the database session
app.dependency_overrides[get_db] = get_db

# Asynchronous event handler for startup
async def startup_event():
    db = SessionLocal()
    try:
        if not get_tables_have_data(engine):
            init_data_on_startup(db)
        else:
            logger.info("Data already exists in the database")
    except Exception as e:
        logger.error("Error during startup: %s", str(e))
    finally:
        db.close()

# Register the event handler with FastAPI
app.add_event_handler("startup", startup_event)

app.include_router(earthquake.router, prefix="/api/v1", tags=["earthquake"])
app.include_router(user.router, prefix="/api/v1", tags=["user"])
