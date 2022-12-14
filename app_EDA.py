import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app() :
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding= 'ISO-8859-1')
    st.text('')
    st.markdown('#### π λ°μ΄ν°νλ μ νμΈ')
    st.dataframe(df.head(3))    

    st.markdown('#### π κΈ°λ³Έ ν΅κ³ λ°μ΄ν°')
    st.dataframe( df.describe() )

    # μ»¬λΌμ μ νν  μ μκ² νλ€. νλμ μ»¬λΌμ μ ννλ©΄,
    # ν΄λΉ μ»¬λΌμ μ΅λκ°, μ΅μκ° λ°μ΄ν°λ₯Ό νλ©΄μ λ³΄μ¬μ€λ€.
    st.markdown('#### π μ΅λ / μ΅μ λ°μ΄ν° νμΈνκΈ°')
    column_list = df.columns[4:]
    selected_column = st.selectbox('μ»¬λΌμ μ ννμΈμ.', column_list)

    if selected_column :
        df_max = df[df[selected_column] == df[selected_column].max()]
        df_min = df[df[selected_column] == df[selected_column].min()]

        st.markdown('##### μ΅λ λ°μ΄ν°')
        st.dataframe(df_max)
        st.markdown('##### μ΅μ λ°μ΄ν°')
        st.dataframe(df_min)


    st.text('')
    st.text('')
    st.text('')
    # μ νν μ»¬λΌμ νμ€ν κ·Έλ¨
    st.subheader('μ»¬λΌ λ³ νμ€ν κ·Έλ¨')
    
    histogram_column = st.selectbox('νμ€ν κ·Έλ¨ νμΈν  μ»¬λΌμ μ ννμΈμ.', column_list)
    my_bins = st.number_input('λΉμ κ°―μλ₯Ό μλ ₯νμΈμ', 10, 30, value= 10, step= 1)


    fig1 = plt.figure()
    plt.title(histogram_column + ' Histogram')
    plt.hist(data= df, x= histogram_column, rwidth = 0.8, bins =my_bins)
    plt.xlabel(histogram_column)
    plt.ylabel('Count')
    st.pyplot(fig1)    


    st.subheader('μκ΄ κ΄κ³ λΆμ')
    selected_list = st.multiselect('μκ΄λΆμμ νκ³ μΆμ μ»¬λΌμ μ ννμΈμ', column_list)
    
    if len(selected_list) >= 2 :
        df_corr = df[ selected_list ].corr()

        fig2 = plt.figure()
        sb.heatmap(data= df_corr, annot= True, fmt='.2f', cmap='coolwarm', vmin = -1, vmax= 1, linewidths= 0.5)
        st.pyplot(fig2)