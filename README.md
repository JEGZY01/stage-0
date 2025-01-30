# HNG12 Stage 0 Task

## Project Description
This project implements a simple public API using FastAPI. The API serves the following information in JSON format:

- The registered email address used for the HNG12 Slack workspace
- The current date and time in ISO 8601 format (UTC)
- The GitHub URL of the project's repository

This project serves as a demonstration of building a backend API with FastAPI, managing GET requests, and ensuring the 
API is deployed to a publicly accessible endpoint.

## Setup Instructions

To run this project locally, follow these steps:

### Prerequisites
Make sure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

### Steps to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   
2. Navigate to the project directory:
   ```bash
   cd your-repo
   
3. Install the required dependencies:
   ```bash
    pip install fastapi uvicorn

4. Run the FastAPI server:
   ```bash
    uvicorn main:app --reload
