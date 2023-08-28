from typing import List, Literal, TypedDict

import pandas as pd
from pycaret.classification import load_model, predict_model


class _TypeConfig(TypedDict):
    file: str


Sex = Literal["男", "女"]


class AgeDef:
    def __init__(self, start: int, end: int, id_: int) -> None:
        self.start = start
        self.end = end
        self.__id = id_

    def is_contain(self, age: int):
        return self.start <= age and age < self.end

    def to_str(self):
        return f"{self.start}～{self.end}"

    def to_id(self):
        return self.__id


ages = [
    (25, 30, 1),
    (30, 35, 2),
    (35, 40, 3),
    (40, 45, 4),
    (45, 50, 5),
    (50, 55, 6),
    (55, 60, 7),
    (60, 65, 8),
    (65, 70, 9),
    (70, 80, 10),
    (85, 90, 11),
]
age_defs = [AgeDef(*a) for a in ages]


def convert_age(age: int):
    for age_def in age_defs:
        if age_def.is_contain(age):
            return age_def
    raise Exception("Age definition not found")


class FatigueLevelDef:
    def __init__(self, desc: str, id_: int) -> None:
        self.desc = desc
        self.__id = id_

    def to_id(self):
        return self.__id


fatigue_levels = [
    # ("要注意", 1),
    # ("やや注意", 2),
    # ("注意", 3),
    # ("平常", 4),
    # ("判定できない", 5),
    ("ぐったり", 6),
    ("すっきり", 7),
    ("ぼんやり", 8),
    ("データなし(未測定)", 9),
]
fatigue_level_defs = [FatigueLevelDef(*a) for a in fatigue_levels]


def convert_fatigue_level(fatigue_level: str):
    for fl in fatigue_level_defs:
        if fl.desc == fatigue_level:
            return fl.to_id()
    raise Exception("Fatigue level definition not found")


class _TypeInputVital(TypedDict):
    body_temp: List[float]
    spo2: List[float]
    sys: List[float]
    dia: List[float]
    fatigue_lh: List[float]
    fatigue_deviation: List[float]
    fatigue_level: List[str]


class _TypeInputCar(TypedDict):
    load: List[int]
    depth: List[int]
    width: List[int]
    height: List[int]


class _TypeInputUser(TypedDict):
    age: List[int]
    sex: List[Sex]


class ModelInput(TypedDict):
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

    def __call__(self, data: ModelInput) -> float:
        input_car = {
            **data["car"],
            "total_weight": data["car"]["load"],
            "length": data["car"]["depth"],
        }
        input_user = {
            **data["user"],
            "generation_id": convert_age(data["user"]["age"][0]).to_id(),
            "sex_id": 1 if data["user"]["sex"] == "男" else 2,
        }
        input_vital = {
            **data["vital"],
            "fatigue_level_id": convert_fatigue_level(
                data["vital"]["fatigue_level"][0]
            ),
        }

        df_car = pd.DataFrame.from_dict(dict(input_car))
        df_user = pd.DataFrame.from_dict(dict(input_user))
        df_vital = pd.DataFrame.from_dict(dict(input_vital))

        inputs = pd.concat([df_car, df_user, df_vital], axis=1)
        if self.__verbose:
            print(inputs)

        return (
            predict_model(
                self.__model,
                inputs,
                raw_score=True,
            )["prediction_score_1"]
            .to_numpy()
            .tolist()[0]
        )


if __name__ == "__main__":
    m = Model({"file": "./models/trial03_2_v001"}, verbose=False)

    data: ModelInput = {
        "car": {
            "load": [2040],
            "depth": [468],
            "width": [169],
            "height": [186],
        },
        "user": {"age": [47], "sex": ["男"]},
        "vital": {
            "body_temp": [37.5],
            "spo2": [98.0],
            "sys": [140.0],
            "dia": [96.0],
            "fatigue_lh": [2.06],
            "fatigue_deviation": [70.0],
            "fatigue_level": ["ぼんやり"],
        },
    }
    result = m(data)
    print(result)
    hash(m)
