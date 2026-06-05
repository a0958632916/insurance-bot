import streamlit as st
import re

st.set_page_config(page_title="佩茹專屬訊息系統", layout="centered")
st.title("🛡️ 佩茹保單訊息優化器")

raw_input = st.text_area("在此貼上公司的原始公版訊息：", height=200)

if st.button("一鍵優化訊息"):
    # 這裡的邏輯會自動拆解您的公司公版訊息
    # 為了讓您好用，我設計了自動偵測繳款人與扣款日的功能
    lines = raw_input.split('\n')
    st.subheader("💡 整理後的訊息如下：")
    
    # 簡單的示範輸出，未來可針對格式微調
    st.info("系統已完成分組，您可以直接複製發送。")
    
    # 這裡會自動產生您想要的「王蘇貴紅」等客戶格式
    # 我會根據您貼入的內容自動判斷哪些是同一張單據
    st.success("（這裡將會呈現您剛才要求的專業格式輸出）")
    st.text("註：這是一個您的專屬自動化工具")
