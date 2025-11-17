import streamlit as st
import numpy as np
import pandas as pd

# --------------------------------
# 페이지 전체 스타일 커스터마이징
# --------------------------------
st.set_page_config(page_title="ALL DAY STRESS OUT", layout="centered")

# 배경 / 글꼴 / 카드 CSS
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Noto Sans KR', sans-serif;
}

body {
    background: linear-gradient(135deg, #eef2f3 0%, #dfe9f3 100%);
}

.title-container {
    padding: 25px;
    text-align: center;
    background: white;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.card {
    background: #ffffff;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# 헤더 타이틀 카드
# --------------------------------
st.markdown("""
<div class="title-container">
    <h1 style="margin-bottom:5px;">🧠 ALL DAY STRESS OUT</h1>
    <p style="font-size:17px; color:#333;">
        스트레스 지수를 빠르게 예측하는 경량 AI Web App
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("설치 없이 바로 실행되는 초경량 스트레스 예측 모델 ✨")

# --------------------------------
# 예측 함수
# --------------------------------
def predict_tomorrow(last_seq):
    return np.mean(last_seq)

def predict_week(last_seq):
    preds = []
    seq = last_seq.copy()

    for _ in range(7):
        tomorrow = np.mean(seq)
        preds.append(tomorrow)
        seq = np.append(seq[1:], tomorrow)

    return preds

# --------------------------------
# 입력 카드 UI
# --------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📥 최근 7일 자율신경활성도 입력")
user_input = st.text_input(
    "7일치 값을 쉼표로 입력하세요",
    "50, 52, 55, 53, 51, 49, 50"
)

predict_btn = st.button("🔮 예측하기")

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------
# 예측 결과 출력 카드
# --------------------------------
if predict_btn:
    try:
        last_seq = np.array(list(map(float, user_input.split(","))))

        if len(last_seq) != 7:
            st.error("⚠️ 정확히 7개의 숫자를 입력해야 합니다!")

        else:
            tomorrow = predict_tomorrow(last_seq)
            week = predict_week(last_seq)

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📊 예측 결과")

            st.success(f"🎯 **내일의 스트레스 지수: {tomorrow:.2f}**")

            df_week = pd.DataFrame({
                "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
                "Predicted Stress": week
            })

            st.line_chart(df_week, x="Day", y="Predicted Stress")

            st.markdown('</div>', unsafe_allow_html=True)

    except:
        st.error("입력 형식이 올바르지 않습니다! (예시: 50,52,53,51,49,50,52)")
