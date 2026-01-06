import streamlit as st
import random
import time

# 게임 초기화
st.title("간단한 타겟 게임")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0  # 초기 점수
if "target_position" not in st.session_state:
    st.session_state.target_position = (random.randint(100, 700), random.randint(100, 400))  # 타겟의 랜덤 위치

# 게임 시작 메시지
st.write("화면에서 타겟을 클릭하여 점수를 얻으세요!")

# 타겟 클릭 시 점수 업데이트
def on_target_click():
    st.session_state.score += 1  # 점수 증가
    st.session_state.target_position = (random.randint(100, 700), random.randint(100, 400))  # 새로운 타겟 위치

# 타겟을 화면에 표시
st.markdown(
    f"""
    <div style="position: absolute; left: {st.session_state.target_position[0]}px; top: {st.session_state.target_position[1]}px;
    width: 50px; height: 50px; background-color: red; border-radius: 50%; cursor: pointer;" 
    onclick="window.location.reload();"></div>
    """,
    unsafe_allow_html=True,
)

# 현재 점수 표시
st.write(f"현재 점수: {st.session_state.score}")

# 게임 반복 실행을 위해 버튼 추가
if st.button("타겟 클릭!"):
    on_target_click()
    time.sleep(0.5)  # 타겟을 클릭하면 잠시 대기 후 새로운 타겟을 생성
