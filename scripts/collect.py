import os
import shutil
from logging import getLogger
from pathlib import Path

logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))

BASE_DIR = Path("./data").resolve()


def collect(resource: str):
    for dir in BASE_DIR.iterdir():
        if not dir.name.startswith(resource + "_") or dir.is_file():
            continue
        for file in dir.iterdir():
            if file.name.endswith(".csv"):
                shutil.move(file, BASE_DIR / resource / file.name)
                logger.debug("processed file: " + file.name)
            else:
                logger.warning("skipped file: " + file.name)


resources = ["vitals", "events", "sensors_acc", "sensors_map", "driving_vitals"]

for r in resources:
    collect(r)
