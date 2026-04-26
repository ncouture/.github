# -*- encoding: utf-8 -*-

import os
import uvicorn

from fastapi import FastAPI

from google.adk.cli.fast_api import get_fast_api_app

# Point this to the directory containing your .yaml AgentConfig files
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
AGENT_DIR = os.path.join(MAIN_DIR, "ayc")  # Agent YAML Config

# The ADK helper automatically creates a FastAPI app, parses your agents,
# and sets up the required API routes and session management.
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=True,  # Set to True to also serve the built-in ADK developer web interface
)


# You can still add your own custom FastAPI endpoints alongside the ADK agents
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ADK Multi-Agent Service"}


if __name__ == "__main__":
    # Serve the application using uvicorn
    print("Starting ADK Server on http://0.0.0.0:8000")
    print(f"Make sure your .yaml files are in: {AGENT_DIR}")
    uvicorn.run("agent_config_server:app", host="0.0.0.0", port=8000, reload=True)
