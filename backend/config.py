import os
from pathlib import Path

CONFIG = {
    "DB_HOST": os.getenv("BE_DB_HOST", "localhost"),
    "BASE_DIR": os.getenv("BE_BASE_DIR", Path(__file__).parent.absolute()),
    # mitigating locking up the app by getting a complete db dump in one go
    "MAX_PAGINATION": int(os.getenv("BE_MAXIMUM_PAGINATION", 20)),
}
