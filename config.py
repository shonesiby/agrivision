"""Application configuration loader with zero-dependency .env support."""

import os


def load_env_file(env_path=".env"):
    """Load key=value pairs from a local .env file without overriding existing env vars."""
    if not os.path.exists(env_path):
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


load_env_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "disease_iot_agriculture")

FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")


def get_gemini_api_key(feature_env_var=None):
    """Return the feature-specific Gemini API key or fall back to GEMINI_API_KEY."""
    if feature_env_var:
        val = os.environ.get(feature_env_var, "").strip()
        if val:
            return val
    return os.environ.get("GEMINI_API_KEY", "").strip()
