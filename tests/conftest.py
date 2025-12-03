"""
Pytest configuration for the NOAA FastAPI service.

Ensures the generated `openapi_client` package (in `noaa_client/`) is
importable without needing a separate pip install.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOAA_CLIENT_DIR = ROOT / "noaa_client"

if str(NOAA_CLIENT_DIR) not in sys.path:
    sys.path.insert(0, str(NOAA_CLIENT_DIR))


