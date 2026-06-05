import streamlit as st
import re
from collections import defaultdict

st.set_page_config(page_title="佩茹保單訊息優化器", layout="centered")
st.title("🛡️ 佩茹保單訊息優化器")

raw_input = st.text_area("請貼上公司公版訊息（支援多筆）：", height=200)

if st.button("一鍵優化訊息"):
    # 針對含有被保險人姓名格式的精確抓取
    # 抓取範例：(姓名)保單：123 | 保費：$456
    pattern = r'親愛的保戶(.*?)您好：.*?保單(\d{3}\*+\d{3}).*?即將於(.*?)\s.*?指定帳戶\((.*?)\).*?保費台幣([\d,]+)元'
    # 額外抓取括號內的被保險人名稱
    name_pattern = r'①\s*\((.*?)\)保單：(\d{3}\*+\d{3})'
    
    matches = re.findall(pattern, raw_input, re.DOTALL)
    name_matches = dict(re.findall(name_pattern, raw_input)) # 建立 {保單號: 被保險人} 的對照表

    groups = defaultdict(list)
    for name, policy, date, account, amount in matches:
        clean_amount = int(amount.replace(',', ''))
        # 若有抓到對應的被保險人則加上，否則留空
        insured = name_matches.get(policy, "")
        groups[(name.strip(), date.strip(), account.strip())].append({
            'policy': policy,
            'amount': clean_amount,
            'insured': insured
        })
    
    st.subheader("💡 整理後的訊息如下：")
    
    for (name, date, account), items in groups.items():
        total = sum(item['amount'] for item in items)
        
        msg = f"親愛的保戶 {name} 您好：\n"
        msg += f"【國泰人壽】提醒您，以下保單即將於 {date} 自指定帳戶（{account}）進行扣款：\n"
        
        for i, item in enumerate(items, 1):
            insured_str = f" ({item['insured']})" if item['insured'] else ""
            msg += f" ①{insured_str} 保單：{item['policy']} | 保費：${item['amount']:,}\n"
            
        msg += f"\n合計扣款總額：${total:,}\n"
        msg += f"請您於 {date.split('/')[0]}/{int(date.split('/')[1])-1} 前確認該帳戶餘額充足，以確保扣款順利。\n"
        msg += "若有任何相關疑問，歡迎隨時與您專屬的保險顧問 林佩茹 聯繫，謝謝！"
        
        st.code(msg, language="text")
        st.divider()
