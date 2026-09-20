import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from the .env file in the project root
load_dotenv()

# Initialize the FastAPI application
app = FastAPI(
    title="SIT Mangaluru Admissions Agent API",
    description="Backend API powering the college admissions chatbot widget.",
    version="0.1.0",
)

# CORS (Cross-Origin Resource Sharing) configuration:
# This allows our embeddable widget (hosted on any website or origin)
# to make HTTP requests to this backend without getting blocked by browser security.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; allows any domain to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Allows headers like Content-Type
)


@app.get("/")
def root():
    """Welcome endpoint confirming the server is accessible."""
    return {
        "status": "online",
        "service": "SIT Mangaluru Admissions Agent API",
        "docs_url": "/docs",
    }


@app.get("/api/health")
def health_check():
    """Health check endpoint to verify backend status and environment configuration."""
    api_key_set = bool(os.getenv("ANTHROPIC_API_KEY") and os.getenv("ANTHROPIC_API_KEY") != "your_anthropic_api_key_here")
    return {
        "status": "healthy",
        "anthropic_key_configured": api_key_set,
        "environment": os.getenv("ENVIRONMENT", "development"),
    }
