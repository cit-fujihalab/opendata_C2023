import logging
import os
import shutil

for dir in os.listdir("./data"):
    if not dir.startswith("vitals_"):
        continue
    for file in os.listdir("./data/" + dir):
        if file.endswith(".csv"):
            shutil.move("./data/" + dir + "/" + file, "./data/vitals/")
        else:
            logging.warning("skipped file: " + "./data/" + dir + "/" + file)
