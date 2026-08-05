import os
from datetime import datetime

LOG_FILE = "logs/agent_log.txt"

def write_log(stage, message):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now()}] {stage}: {message}\n")