import streamlit as st
import re

st.set_page_config(page_title="佩茹保單訊息優化器", layout="centered")
st.title("🛡️ 佩茹保單訊息優化器")

raw_input = st.text_area("在此貼上公司的原始公版訊息：", height=200)

if st.button("一鍵優化訊息"):
    # 這裡加入解析與處理的邏輯
    st.subheader("💡 整理後的訊息如下：")
    
    # 簡單的提取邏輯：尋找保單號、日期、金額
    policies = re.findall(r'保單(\d{4}\*\*\*\*\d{3})即將於(\d{3}/\d{1,2}/\d{1,2}).*?保費台幣([\d,]+)元', raw_input)
    bank_info = re.search(r'指定帳戶\((.*?)\)', raw_input)
    
    if policies:
        bank = bank_info.group(1) if bank_info else "指定帳戶"
        total = sum([int(p[2].replace(',', '')) for p in policies])
        
        st.info("已成功解析保單，請複製下方訊息：")
        output = f"親愛的保戶 您好：\n【國泰人壽】提醒您，以下保單將於 {policies[0][1]} 自指定帳戶({bank})進行扣款，合計總額：${total:,}\n\n"
        for i, p in enumerate(policies, 1):
            output += f"{i}. 保單：{p[0]} | 保費：${p[2]}\n"
        output += "\n請於扣款日前一日確認帳戶存足款項。若有疑問，請與專屬保險顧問 林佩茹 聯繫，謝謝！"
        
        st.code(output, language='text')
    else:
        st.warning("請確認貼上的文字是否包含標準的保單格式。")
