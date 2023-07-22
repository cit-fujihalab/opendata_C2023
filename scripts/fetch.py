import abc
import datetime as dt
import logging
import multiprocessing
import os
import queue
import threading
import time
import zipfile
from typing import Any

import requests


class BaseApi(abc.ABC):
    def __init__(self, key: str, base_uri: str) -> None:
        self.key = key
        self.base_uri = base_uri

    @property
    def resource_name(self) -> str:
        raise NotImplementedError()

    def get(self, zip_name: str):
        TEMP_DIR = "./tmp"
        OUT_DIR = "./data"
        params = {"acl:consumerKey": self.key}

        logging.info("fetching " + zip_name)

        res = requests.get(
            self.base_uri + "/" + self.resource_name + "/" + zip_name,
            params=params,
            stream=True,
            timeout=(10.0, 60.0),
        )
        res.raise_for_status()

        q: "queue.Queue[Any]" = queue.Queue(0)
        is_finished = False

        def write():
            os.makedirs(TEMP_DIR, exist_ok=True)
            with open(TEMP_DIR + "/" + zip_name, "wb") as f:
                while True:
                    if q.empty() and is_finished:
                        return
                    if q.empty():
                        time.sleep(0.1)
                        continue

                    chunk = q.get_nowait()
                    f.write(chunk)
                    f.flush()
                    q.task_done()

        t = threading.Thread(target=write)
        t.start()

        for chunk in res.iter_content(chunk_size=10**7):
            q.put(chunk)

        is_finished = True
        q.join()

        logging.info("fetched " + zip_name)

        def async_extract():
            with zipfile.ZipFile(TEMP_DIR + "/" + zip_name) as zf:
                for info in zf.infolist():
                    zf.extract(info, path=OUT_DIR + "/" + zip_name.rsplit(".zip", 1)[0])

            os.remove(TEMP_DIR + "/" + zip_name)
            logging.info("extracted " + zip_name)

        p = multiprocessing.Process(target=async_extract)
        p.start()
        return p


class ResourceApi(BaseApi):
    def download(self, date: dt.date):
        self.get(self.resource_name + "_" + date.strftime("%Y%m%d") + ".zip")


class VitalApi(ResourceApi):
    resource_name = "vitals"  # type: ignore


class EventApi(ResourceApi):
    resource_name = "events"  # type: ignore


class PositionApi(ResourceApi):
    resource_name = "sensors_map"  # type: ignore


class SensorAccApi(ResourceApi):
    resource_name = "sensors_acc"  # type: ignore


class DrivingVitalApi(ResourceApi):
    resource_name = "driving_vitals"  # type: ignore


class CarApi(BaseApi):
    resource_name = "masters"  # type: ignore


class UserApi(BaseApi):
    resource_name = "masters"  # type: ignore


if __name__ == "__main__":
    from dotenv import load_dotenv

    BASE_URI = "https://api.daiwa-open-challenge.jp/files"

    LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
    logging.basicConfig(level=LOGLEVEL)

    load_dotenv("./env/.env.dev")

    vital_api = VitalApi(os.environ["API_KEY"], BASE_URI)
    event_api = EventApi(os.environ["API_KEY"], BASE_URI)
    sensor_api = SensorAccApi(os.environ["API_KEY"], BASE_URI)
    position_api = PositionApi(os.environ["API_KEY"], BASE_URI)
    driving_vital_api = DrivingVitalApi(os.environ["API_KEY"], BASE_URI)

    date = dt.datetime(2022, 1, 1)
    while date < dt.datetime(2022, 12, 1):
        for api in [vital_api, event_api, sensor_api, position_api, driving_vital_api]:
            try:
                api.download(date)
            except:
                logging.error(api.resource_name + " " + date.strftime("%Y%m%d"))

        date = date + dt.timedelta(days=1)

    CarApi(os.environ["API_KEY"], BASE_URI).get("master_cars_202301.zip")
    UserApi(os.environ["API_KEY"], BASE_URI).get("master_users_202301.zip")
