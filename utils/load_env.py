from dotenv import load_dotenv
import os

def load_environment():
    load_dotenv()
    required_keys = [
        "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT_NAME",
        "SQL_USERNAME", "SQL_PASSWORD", "SQL_SERVER", "SQL_DATABASE"
    ]
    for key in required_keys:
        if not os.getenv(key):
            raise ValueError(f"Missing required environment variable: {key}")
