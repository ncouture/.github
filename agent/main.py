# -*- encoding: utf-8 -*-

from version import __version__

version = __version__

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests

app = FastAPI()

# Configure CORS so your frontend can communicate with this backend
# Update this list with your actual frontend URLs
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


__all__ = [version, __version__]
