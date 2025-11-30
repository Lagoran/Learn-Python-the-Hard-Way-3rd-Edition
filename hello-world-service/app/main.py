import logging

logger = logging.getLogger(__name__)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Hello World Service",
    description="A simple FastAPI service that displays 'Hello world!' on a web page",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to specific origins in production
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello world!"}


@app.get("/html", response_class=HTMLResponse)
async def read_html():
    """HTML endpoint that returns Hello world! as HTML"""
    return "<html><body><h1>Hello world!</h1></body></html>"
