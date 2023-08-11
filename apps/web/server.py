import streamlit as st

from pycaret.datasets import get_data
from pycaret.regression import *

data = get_data("boston")

@st.cache_resource()
def create_model_cache(estimator):
    return create_model(estimator)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

pipe = setup(data, target="medv", html=False)

@st.cache_resource()
def ensemble_model_cache(estimators):
    _model = blend_models(estimator_list=[create_model_cache(estimator) for estimator in estimators])
    return ensemble_model(_model)

model = ensemble_model_cache(["et", "lightgbm"])

plot_model(model, plot="cooks", display_format="streamlit")

predictions = predict_model(model)
st.write(predictions)



