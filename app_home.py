import streamlit as st

def run_home_app() :

    img2 = st.sidebar.image('https://cdn-pro-web-209-212-godomall.spdycdn.net/malb2b1_godomall_com/data/goods/detail/12203_Detail0.jpg')
    img3 = st.sidebar.image('http://www.carguy.kr/news/photo/201908/37699_15506_4924.png')
    img1 = st.sidebar.image('https://carssen.com/files/attach/images/40904/915/040/c78421ed0661dd9f01939e48ec56f837.png')

    st.text('')
    st.text('')
    with st.expander('대시보드 설명') :

        st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
        st.text('데이터분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해줍니다.')

    st.text('')
    
    img = 'https://m.renaultkoream.com/new/model/overview_res/img/xm22/xm3_inspire.jpg'
    st.image(img)


