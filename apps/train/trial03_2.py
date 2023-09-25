# %% import
import os

import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from pycaret.classification import (
    compare_models,
    create_model,
    evaluate_model,
    finalize_model,
    predict_model,
    save_model,
    setup,
    tune_model,
)
from sklearn.model_selection import train_test_split

DATASET_FILE = os.environ["DATASET_FILE"]

x = pd.read_csv(DATASET_FILE)

x_train, x_unseen = train_test_split(
    x, test_size=0.05, stratify=x["case"], random_state=786
)
x_train = x_train.reset_index(drop=True)
x_unseen = x_unseen.reset_index(drop=True)

# %%
s = setup(
    data=x_train,
    target="case",
    numeric_features=[
        "body_temp",
        "spo2",
        "sys",
        "dia",
        "fatigue_lh",
        "fatigue_deviation",
        "total_weight",
        "length",
        "width",
        "height",
    ],
    categorical_features=["sex_id", "generation_id", "fatigue_level_id"],
    ignore_features=["user_id"],
    numeric_imputation="median",
    categorical_imputation="mode",
    fix_imbalance=True,
    fix_imbalance_method=RandomUnderSampler(
        sampling_strategy="majority", random_state=42
    ),
    normalize=True,
    session_id=324,
)

# %%
best = compare_models()

# %%
model = create_model("lr")
# lightgbm or lr

# %%
model = tune_model(model)

# %%
evaluate_model(model)

# %%
final_model = finalize_model(model)

# %%
p = predict_model(final_model, data=x_unseen)

# %%
p.to_csv("./out/pred.csv")

# %%
save_model(final_model, os.environ["MODEL_FILE"])

# %%
