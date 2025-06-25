import streamlit as st
import pandas as pd
from streamlit import columns

st.title("Data Dashboard")

upload_file=st.file_uploader("CSV formatında verinizi yükleyiniz.",type="csv")

if upload_file:
    df=pd.read_csv(upload_file)
    st.subheader("Veri Setiniz: ")
    st.write(df.head())

    st.subheader("Veri Filtreleme: ")
    columns=df.columns.tolist()

    selected_column=st.selectbox("Kolon Seçiniz",columns)
    filter_value=st.text_input("Bir değer giriniz")

    if selected_column and filter_value:
        filtered_df=df[df[selected_column].astype(str)==filter_value]
        st.write(filtered_df)
    st.subheader("Veri Görselleştirme: ")
    X_column=st.selectbox("X ekseni için bir kolon seçiniz.",columns)
    y_column=st.selectbox("Y ekseni için bir kolon seçiniz.",columns)

    button=st.button("Grafik Çiz")

    if button:
        st.line_chart(df,x=X_column,y=y_column)