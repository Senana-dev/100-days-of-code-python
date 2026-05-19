import streamlit as st

st.title("💸 Tip Calculator")
st.subheader("Hi Jeffrey! Look at my first Python app! ❤️")
st.write("Enter the details below to calculate the split bill.")

bill = st.number_input("What was the total bill? ($)", min_value=0.0, value=150.0, step=0.1)

tip = st.selectbox("What percentage tip would you like to give?", [10, 12, 15, 20])

people = st.number_input("How many people to split the bill?", min_value=1, value=2, step=1)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_per_person = round(bill_per_person, 2)

st.markdown("---")  # 구분선
st.success(f"### 💰 Each person should pay : **${final_per_person}**")
st.balloons()  # 축하 풍선 애니메이션 효과!