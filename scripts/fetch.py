import os

import datetime as dt
import abc
import requests
import logging
import zipfile

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


class Api(abc.ABC):
    BASE_URI = "https://api.daiwa-open-challenge.jp/files"

    def __init__(self, key: str) -> None:
        self.key = key

    @property
    @abc.abstractmethod
    def resource_name(self) -> str:
        return ""

    def get(self, date: dt.datetime):
        params = {"acl:consumerKey": self.key}
        url = (
            self.BASE_URI
            + "/"
            + self.resource_name
            + "/"
            + self.resource_name
            + "_"
            + date.strftime("%Y%m%d")
            + ".zip"
        )
        res = requests.get(url, params=params, stream=True, timeout=(10.0, 60.0))

        filename = url.split("/")[-1]
        with open("./data/" + filename, "wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

        with zipfile.ZipFile("./data/" + filename) as zf:
            zf.extractall("./data/" + filename.rsplit(".zip", 1)[0])

        os.remove("./data/" + filename)


class EventApi(Api):
    resource_name = "events"  # type: ignore


class SensorAccApi(Api):
    resource_name = "sensors_acc"  # type: ignore


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv("./env/.env.dev")
    event_api = EventApi(os.environ["API_KEY"])
    event_api.get(date=dt.datetime(2022, 1, 1))

    sensor_api = SensorAccApi(os.environ["API_KEY"])
    sensor_api.get(date=dt.datetime(2022, 9, 4))
