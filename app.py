import streamlit as st
import re

st.set_page_config(page_title="佩茹保單訊息優化器", layout="centered")
st.title("🛡️ 佩茹保單訊息優化器")

raw_input = st.text_area("在此貼上公司的原始公版訊息：", height=200)

if st.button("一鍵優化訊息"):
    st.subheader("💡 整理後的訊息如下：")
    
    # 這裡加入簡單的解析邏輯：尋找保單號碼與金額
    policies = re.findall(r'保單(\d{3}\*+\d{3})', raw_input)
    amounts = re.findall(r'保費台幣([\d,]+)元', raw_input)
    
    if policies:
        st.success("已成功偵測到保單資料，請確認下方內容：")
        for p, a in zip(policies, amounts):
            st.write(f"• 保單號：{p} | 保費：{a} 元")
        
        # 顯示您的專業署名
        st.write("---")
        st.write("若有任何問題，請與您的專屬保險顧問 **林佩茹** 聯繫，謝謝！")
    else:
        st.warning("請確認貼上的文字是否包含標準的保單格式。")
