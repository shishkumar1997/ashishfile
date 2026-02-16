from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from app.database import Base, engine
from app.routers import users


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management System",
    description="FastAPI-based user management system with JWT authentication",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Favicon handler to prevent 404 errors
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)

# Include routers
app.include_router(users.router, prefix="/api", tags=["users"])
