import infer
import streamlit as st


@st.cache_resource()
def get_model():
    return infer.Model(cfg={"file": "./models/save_test"})


model = get_model()

age = st.number_input("Age", min_value=25, max_value=69, format="%d")
sex = st.selectbox("年齢", ("男", "女"), index=0) or "男"


# plot_model(model, plot="cooks", display_format="streamlit")

# predictions = predict_model(model)
data: infer.ModelInput = {
    "car": {
        "car_load": [1600],
        "max_load": [0],
        "load": [2040],
        "depth": [468],
        "width": [169],
        "height": [186],
        "ventilation": [3.99],
    },
    "user": {"age": [int(age)], "sex": [sex]},
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
score = model(data)
st.write(score)
