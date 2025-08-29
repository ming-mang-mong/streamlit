import streamlit as st
st.caption('text 참고사이트: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app')

import streamlit as st

st.set_page_config(page_title="Demo", layout="wide")

# 사이드바 페이지 선택
page = st.sidebar.radio("페이지", ["사용자 정보", "추천", "링크"], index=0)

def home_page():
    st.title("사용자 정보")

    # 2. Radio Button
    # 라디오 버튼 (하나만 선택 가능)
    st.header('사용자 직업')
    job = st.radio('직업이 무엇인가요?', ('학생', '직장인', '프로게이머', '크리에이터', '기타'))

    if job == '학생':
        st.markdown("모니터 추천: 가성비 휴대용 또는 눈 편한 IPS  \n키보드 추천: 저렴하고 기본 성능 좋은 가벼운 키보드  \n마우스 추천: 휴대성 좋고 저렴한 마우스")
    elif job == '직장인':
        st.markdown("모니터 추천: 고해상도, 색감 좋은 IPS  \n키보드 추천: 업무 효율성·편안함 강조  \n마우스 추천: 편안한 인체공학형 마우스")
    elif job == '프로게이머':
        st.markdown("모니터 추천: 초고주사율 및 반응속도 우수  \n키보드 추천: 응답속도 빠른 게이밍 모델  \n마우스 추천: 경량·정밀·고감도 게이밍 마우스")
    else:
        st.markdown("모니터 추천: 일반 용도 무난하게 쓸 수 있는 실속형 모니터  \n키보드 추천: 보편적인 기능의 사무용 키보드  \n마우스 추천: 가성비 좋은 기본 마우스")


def analysis_page():
    st.title("추천")

    tab1, tab2, tab3 = st.tabs(["노트북", "키보드", "마우스"])
    with tab1:
        st.write("노트북 추천")
    with tab2:
        st.write("키보드 추천")
    with tab3:
        st.write("마우스 추천")

def settings_page():
    st.title("링크")


# 간단 라우팅
if page == "사용자 정보":
    home_page()


elif page == "추천":
    analysis_page()

elif page == "링크":
    settings_page()


