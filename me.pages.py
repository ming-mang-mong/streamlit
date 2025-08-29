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
    elif job == '크리에이터':
        st.markdown("모니터 추천: 큰 화면, 고해상도, 색재현 우수한 모델  \n키보드 추천: 기계식·타건감 좋은 커스터마이징 키보드  \n마우스 추천: 정밀 포인팅 가능, 추가 버튼 많은 마우스")
    else:
        st.markdown("모니터 추천: 일반 용도 무난하게 쓸 수 있는 실속형 모니터  \n키보드 추천: 보편적인 기능의 사무용 키보드  \n마우스 추천: 가성비 좋은 기본 마우스")


def analysis_page():
    st.title("추천")

    tab1, tab2, tab3 = st.tabs(["노트북", "키보드", "마우스"])
    with tab1:
        tit = st.selectbox(
            '당신의 직업을 선택하세요.',
            ('학생', '직장인', '프로게이머', '크리에이터', '기타') )
        if tit == '학생':
            st.caption('ViewSonic VA2456a‑MHD')
            st.image('https://www.viewsonic.com/media/catalog/product/cache/b1231e477ffebecb36748a51c37e27d3/2/4/24mon-con1798-prd-va2456a_front_2000x2000.jpg')
        elif tit == '직장인':
            st.caption('Dell Ultrasharp U2724DE')
            st.image('https://img.danawa.com/prod_img/500000/786/463/img/31463786_1.jpg')
        elif tit == '프로게이머':
            st.caption('LG UltraGear 32GS95UE-B')
            st.image('https://www.lge.co.kr/kr/images/monitors/md10459827/gallery/medium01.jpg')
        elif tit == '크리에이터':
            st.caption('삼성 OLED 울트라와이드')
            st.image('https://m.builec.com/web/product/big/thumbnail/P000ILWP.jpg')
        else:
            st.caption('MSI Pro MP225V')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjCPUjMPjIIDYyVRGK48swmsUcGxD_x_-LXQ&s')

    with tab2:
        tit = st.selectbox(
            '당신의 직업을 선택하세요.',
            ('학생', '직장인', '프로게이머', '크리에이터', '기타') )
        if tit == '학생':
            st.caption('Logitech K120')
            st.image('https://img.danawa.com/prod_img/500000/153/581/img/1581153_1.jpg?shrink=360:360')
        elif tit == '직장인':
            st.caption('Keychron C1 Pro 8K')
            st.image('https://img.danawa.com/prod_img/500000/453/055/img/28055453_1.jpg?_v=20230906110418&shrink=360:360')
        elif tit == '프로게이머':
            st.caption('LG UltraGear 32GS95UE-B')
            st.image('https://www.lge.co.kr/kr/images/monitors/md10459827/gallery/medium01.jpg')
        elif tit == '크리에이터':
            st.caption('삼성 OLED 울트라와이드')
            st.image('https://m.builec.com/web/product/big/thumbnail/P000ILWP.jpg')
        else:
            st.caption('Keychron C1 Pro 8K')
            st.image('https://img.danawa.com/prod_img/500000/453/055/img/28055453_1.jpg?_v=20230906110418&shrink=360:360')

    with tab3:
        tit = st.selectbox(
            '당신의 직업을 선택하세요.',
            ('학생', '직장인', '프로게이머', '크리에이터', '기타') )
        if tit == '학생':
            st.caption('Razer Deathadder Essential')
            st.image('https://img.danawa.com/prod_img/500000/066/395/img/15395066_1.jpg?_v=20230829085935&shrink=360:360')
        elif tit == '직장인':
            st.caption('Logitech MX Master 3S')
            st.image('https://ae01.alicdn.com/kf/Sef4a1f75ee014749ac0dacf88fcb74386.jpg')
        elif tit == '프로게이머':
            st.caption('Razer Cobra Pro')
            st.image('https://assets2.razerzone.com/images/pnx.assets/608eb80ec16513e41c1a62caf1fb9b55/razer-cobra-pro-hero.webp')
        elif tit == '크리에이터':
            st.caption('Razer Pro Click V2')
            st.image('https://assets3.razerzone.com/qdHcEeeQ-CE2ZJe7DPnzn9zSf2E=/500x500/https%3A%2F%2Fmedias-p1.phoenix.razer.com%2Fsys-master-phoenix-images-container%2Fha3%2Fh76%2F9899953717278%2Fpro-click-v2-black-500x500.png')
        else:
            st.caption('Logitech MX Master 3S')
            st.image('https://ae01.alicdn.com/kf/Sef4a1f75ee014749ac0dacf88fcb74386.jpg')

def settings_page():
    st.title("링크")


# 간단 라우팅
if page == "사용자 정보":
    home_page()


elif page == "추천":
    analysis_page()

elif page == "링크":
    settings_page()


