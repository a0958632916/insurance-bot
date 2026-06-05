import streamlit as st
import re
from collections import defaultdict

st.set_page_config(page_title="佩茹保單訊息優化器", layout="centered")
st.title("🛡️ 佩茹保單訊息優化器")

raw_input = st.text_area("請貼上公司公版訊息（支援多筆）：", height=200)

if st.button("一鍵優化訊息"):
    # 這裡使用字典進行分組：key 為 (姓名, 日期, 帳戶)
    groups = defaultdict(list)
    
    # 擴充後的 Pattern：捕獲姓名、保單號、日期、銀行帳號、金額
    pattern = r'親愛的保戶(.*?)您好：.*?保單(\d{3}\*+\d{3}).*?(\d{2}/\d{1,2}).*?\((.*?)\).*?保費台幣([\d,]+)元'
    matches = re.findall(pattern, raw_input, re.DOTALL)
    
    for name, policy, date, account, amount in matches:
        clean_amount = int(amount.replace(',', ''))
        groups[(name.strip(), date.strip(), account.strip())].append({
            'policy': policy,
            'amount': clean_amount
        })
    
    st.subheader("💡 整理後的訊息如下：")
    
    for (name, date, account), items in groups.items():
        total = sum(item['amount'] for item in items)
        
        # 產生優化後的訊息格式
        msg = f"親愛的保戶 **{name}** 您好：\n"
        msg += f"【國泰人壽】提醒您，以下保單即將於 **115/{date}** 自指定帳戶（{account}）進行扣款：\n"
        
        for i, item in enumerate(items, 1):
            msg += f" ① 保單：{item['policy']} | 保費：${item['amount']:,}\n"
            
        msg += f"\n合計扣款總額：**${total:,}**\n"
        msg += f"請您於 **115/{int(date.split('/')[1])-1}** 前確認該帳戶餘額充足，以確保扣款順利。\n"
        msg += "若有任何相關疑問，歡迎隨時與您專屬的保險顧問 林佩茹 聯繫，謝謝！"
        
        st.code(msg, language="text")
        st.divider()
