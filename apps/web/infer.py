from typing import List, Literal, TypedDict

import pandas as pd
from pycaret.classification import load_model, predict_model


class _TypeConfig(TypedDict):
    file: str


class AgeDef:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def is_contain(self, age: int):
        return self.start <= age and age < self.end

    def to_str(self):
        return f"{self.start}～{self.end}"


Sex = Literal["男", "女"]

ages = [
    (25, 30),
    (30, 35),
    (35, 40),
    (40, 45),
    (45, 50),
    (50, 55),
    (55, 60),
    (60, 65),
    (65, 70),
]
age_defs = [AgeDef(*a) for a in ages]


def convert_age(age: int):
    for age_def in age_defs:
        if age_def.is_contain(age):
            return age_def
    raise Exception("Age definition not found")


class _TypeInputVital(TypedDict):
    time_hour: List[int]
    body_temp: List[float]
    spo2: List[float]
    sys: List[float]
    dia: List[float]
    fatigue_lh: List[float]
    fatigue_deviation: List[float]


class _TypeInputCar(TypedDict):
    max_load: List[int]
    car_load: List[int]
    load: List[int]
    depth: List[int]
    width: List[int]
    height: List[int]
    ventilation: List[float]


class _TypeInputUser(TypedDict):
    age: List[int]
    sex: List[Sex]


class _TypeInput(TypedDict):
    vital: _TypeInputVital
    car: _TypeInputCar
    user: _TypeInputUser


class Model:
    def __init__(self, cfg: _TypeConfig, verbose=False):
        self.__cfg = cfg
        self.__model = load_model(cfg["file"])
        self.__verbose = verbose

    def __hash__(self) -> int:
        return hash(self.__cfg.values())

    def __call__(self, data: _TypeInput):
        input_car = data["car"]
        input_user = {
            **data["user"],
            "age": convert_age(data["user"]["age"][0]).to_str(),
        }
        input_vital = data["vital"]

        df_car = pd.DataFrame.from_dict(dict(input_car))
        df_user = pd.DataFrame.from_dict(dict(input_user))
        df_vital = pd.DataFrame.from_dict(dict(input_vital))

        inputs = pd.concat([df_car, df_user, df_vital], axis=1)
        if self.__verbose:
            print(inputs)

        return predict_model(
            self.__model,
            inputs,
            raw_score=True,
        )["prediction_score_1"].to_numpy()


if __name__ == "__main__":
    m = Model({"file": "./models/save_test"}, verbose=True)

    data: _TypeInput = {
        "car": {
            "car_load": [1600],
            "max_load": [0],
            "load": [2040],
            "depth": [468],
            "width": [169],
            "height": [186],
            "ventilation": [3.99],
        },
        "user": {"age": [47], "sex": ["男"]},
        "vital": {
            "time_hour": [5],
            "body_temp": [37.5],
            "spo2": [98.0],
            "sys": [140.0],
            "dia": [96.0],
            "fatigue_lh": [2.06],
            "fatigue_deviation": [70.0],
        },
    }
    result = m(data)
    print(result)
    hash(m)
