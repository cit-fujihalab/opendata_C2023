import infer
import streamlit as st


@st.cache_resource()
def get_model():
    return infer.Model(cfg={"file": "./models/save_test"}, verbose=True)


model = get_model()

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("年齢", min_value=25, max_value=69, format="%d")
    with col2:
        sex = st.selectbox("性別", ("男", "女"), index=0) or "男"

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        max_load = st.number_input(
            "最大積載量 [kg]", min_value=0, format="%d", value=1600, step=10
        )
    with col2:
        car_load = st.number_input(
            "車両重量 [kg]", min_value=0, format="%d", value=6270, step=10
        )
    with col3:
        load = st.number_input(
            "車両総重量 [kg]", min_value=0, format="%d", value=7980, step=10
        )

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        depth = st.number_input("全長 [cm]", min_value=0, format="%d", value=1040, step=10)
    with col2:
        width = st.number_input("全幅 [cm]", min_value=0, format="%d", value=250, step=10)
    with col3:
        height = st.number_input("全高 [cm]", min_value=0, format="%d", value=360, step=10)
    with col4:
        ventilation = st.number_input(
            "全高排気量 [ℓ]", min_value=0.0, format="%.1f", value=6.4
        )

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        time_hour = st.number_input(
            "始業時間(0~23) [時]", min_value=0, max_value=23, format="%d", value=9
        )
    with col2:
        body_temp = st.number_input(
            "体温 [℃]", min_value=0.0, format="%4.1f", value=36.8, step=0.1
        )
    with col3:
        spo2 = st.number_input(
            "血中酸素濃度 ", min_value=0.0, format="%.1f", value=97.5, step=0.1
        )

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sys = st.number_input(
            "最高血圧 ", min_value=0.0, format="%.0f", value=120.0, step=1.0
        )
    with col2:
        dia = st.number_input(
            "最低血圧 ", min_value=0.0, format="%.0f", value=80.0, step=1.0
        )
    with col3:
        fatigue_lh = st.number_input(
            "自律神経バランス", min_value=0.0, format="%2.1f", value=1.4, step=0.1
        )
    with col4:
        fatigue_deviation = st.number_input(
            "自律神経機能の偏差値", min_value=0.0, format="%.1f", value=50.0, step=1.0
        )

data: infer.ModelInput = {
    "car": {
        "car_load": [int(car_load)],
        "max_load": [int(max_load)],
        "load": [int(load)],
        "depth": [int(depth)],
        "width": [int(width)],
        "height": [int(height)],
        "ventilation": [ventilation],
    },
    "user": {"age": [int(age)], "sex": [sex]},
    "vital": {
        "time_hour": [int(time_hour)],
        "body_temp": [body_temp],
        "spo2": [spo2],
        "sys": [sys],
        "dia": [dia],
        "fatigue_lh": [fatigue_lh],
        "fatigue_deviation": [fatigue_deviation],
    },
}
score = model(data)
st.write("ヒヤリハット危険度：{:.0f}%".format(score * 100))
