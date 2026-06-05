import streamlit as st
import re

st.set_page_config(page_title="佩茹保單訊息優化器", layout="centered")
st.title("🛡️ 佩茹保單訊息優化器")

raw_input = st.text_area("請貼上公司公版訊息（支援多筆）：", height=200)

if st.button("一鍵優化訊息"):
    # 提取所有資料的 Pattern
    # 這裡的邏輯會捕捉：客戶名、保單號、日期、銀行/郵局名稱、末四碼、金額
    pattern = r'親愛的保戶(.*?)您好：.*?保單(\d{3}\*+\d{3}).*?(\d{2}/\d{1,2}).*?\((.*?後四碼\d{4})\).*?保費台幣([\d,]+)元'
    matches = re.findall(pattern, raw_input, re.DOTALL)
    
    if matches:
        st.subheader("💡 優化後的訊息：")
        for name, policy, date, bank, amount in matches:
            # 扣款日與提醒日邏輯（簡單處理，可依需求調整）
            # 這裡直接輸出您指定的格式
            msg = f"""
親愛的保戶 **{name.strip()}** 您好：
【國泰人壽】提醒您，您的保單 **{policy}** 即將於 **{date}** 自指定帳戶（**{bank}**）進行扣款，保費金額 **${amount}**。
請您於扣款日前一天確認帳戶餘額充足，以確保扣款順利。若有任何疑問，歡迎隨時與您的專屬保險顧問 **林佩茹** 聯繫，謝謝！
            """
            st.code(msg, language="text")
    else:
        st.warning("請確認貼上的文字是否符合標準公版格式，系統目前未捕捉到完整資訊。")
