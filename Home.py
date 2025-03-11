import streamlit as st

st.set_page_config('HOME')

st.header('EXPLORATORY DATA ANALYSIS')
text_1 = """
This application helps you perform exploratory data analysis on stocks and indices.
"""
st.write(text_1)

container_1 = st.container(border=True)

container_1.page_link(page=r"pages/1_Indices.py",label="**Indices**")
text_2 = """
This option lets you perform EDA on NSE indices.
"""
container_1.page_link(page=r"pages/1_Indices.py",label=text_2)


container_1.page_link(page=r"pages/2_Stocks.py",label="**Stocks**")
text_3 = """
This option lets you perform EDA on NSE Stcoks.
"""
container_1.page_link(page=r"pages/2_Stocks.py",label=text_3)

