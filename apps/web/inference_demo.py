import os

import infer
import streamlit as st

st.set_page_config(page_title="ヒヤリハット危険度予測デモ")


@st.cache_resource()
def get_model():
    return infer.Model(
        cfg={"file": os.environ["MODEL_FILE"], "verbose": True},
    )


model = get_model()

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("年齢", min_value=25, max_value=69, format="%d")
    with col2:
        sex = st.selectbox("性別", ("男", "女"), index=0) or "男"

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        depth = st.number_input(
            "全長 [cm]", min_value=0, format="%d", value=1040, step=10
        )
    with col2:
        width = st.number_input("全幅 [cm]", min_value=0, format="%d", value=250, step=10)
    with col3:
        height = st.number_input(
            "全高 [cm]", min_value=0, format="%d", value=360, step=10
        )
    with col4:
        load = st.number_input(
            "車両総重量 [kg]", min_value=0, format="%d", value=7980, step=10
        )

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        body_temp = st.number_input(
            "体温 [℃]", min_value=0.0, format="%4.1f", value=36.8, step=0.1
        )
    with col2:
        spo2 = st.number_input(
            "血中酸素濃度 ", min_value=0.0, format="%.1f", value=97.5, step=0.1
        )
    with col3:
        sys = st.number_input(
            "最高血圧 ", min_value=0.0, format="%.0f", value=120.0, step=1.0
        )
    with col4:
        dia = st.number_input(
            "最低血圧 ", min_value=0.0, format="%.0f", value=80.0, step=1.0
        )

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        fatigue_lh = st.number_input(
            "自律神経バランス", min_value=0.0, format="%2.1f", value=1.4, step=0.1
        )
    with col2:
        fatigue_deviation = st.number_input(
            "自律神経機能の偏差値", min_value=0.0, format="%.1f", value=50.0, step=1.0
        )

fatigue_level = (
    st.selectbox("自律神経レベル", [fl.desc for fl in infer.fatigue_level_defs], index=0)
    or "0"
)


data: infer.ModelInput = {
    "car": {
        "load": [int(load)],
        "depth": [int(depth)],
        "width": [int(width)],
        "height": [int(height)],
    },
    "user": {"age": [int(age)], "sex": [sex]},
    "vital": {
        "body_temp": [body_temp],
        "spo2": [spo2],
        "sys": [sys],
        "dia": [dia],
        "fatigue_lh": [fatigue_lh],
        "fatigue_deviation": [fatigue_deviation],
        "fatigue_level": [fatigue_level],
    },
}
score = model(data)
st.write("ヒヤリハット危険度：{:.0f}%".format(score * 100))
