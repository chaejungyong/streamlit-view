import streamlit as st

view = [100,150,30]
st.write('# 유튜브 조회수')
st.write('## 설명')
view
st.write('## 막대챠트')
st.bar_chart(view)
import pandas as pd
sview=pd.Series(view)
sview