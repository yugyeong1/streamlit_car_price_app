import streamlit as st
import numpy as np
import joblib


def run_ml_app() :
    st.subheader('자동차 금액 예측')

#성별 여자이고, 나이는 50, 연봉은 4만달러, 카드빚 5만달러
# 자산은 20만 달라이면 이 사람은 얼마짜리 차를 살 것인가?

# 성별, 나이, 연봉, 카드빚, 자산을 유저한테 모두 입력받아서
# 자동차 구매 금액 예측하세요.

    gender = st.radio('성별을 선택하세요', ['여자', '남자'])

    if gender == '여자' :
        gender = 1

    elif gender == '남자' :
        gender = 0

    age = st.number_input('나이를 입력하세요', 18 , 100)
    salary = st.number_input('연봉을 입력하세요', 10000, 1000000)
    card_debt = st.number_input('카드빚을 입력하세요', 0, 1000000)
    net_Worth = st.number_input('자산을 입력하세요', 1000, 10000000)


    new_data = np.array([gender, age, salary, card_debt, net_Worth])
    new_data = new_data.reshape(1,5)

    regressor = joblib.load('regressor.pkl')
    y_pred = regressor.predict(new_data)


    # 반올림할 데이터와, 몇번째 자리까지 보여줄지 소숫점을 적어준다.
    y_pred = round(y_pred[0] , 1)

    if y_pred < 0 :
        st.info('입력한 데이터로는 금액을 예측하기 어렵습니다')

    else :
        st.info('예측한 자동차 금액은 {} 입니다'.format(y_pred))

  