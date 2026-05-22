import streamlit as st
import random

# 1. char set
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 2. titles
st.title("🔐 PyPassword Generator")
st.subheader("Create a strong password for your security! 😉")
st.markdown("---")

# 3. user input
st.write("### ⚙️ Configure Password Length")

nr_letters = st.slider("How many letters would you like?", min_value=0, max_value=20, value=8)
nr_symbols = st.slider("How many symbols would you like?", min_value=0, max_value=10, value=2)
nr_numbers = st.slider("How many numbers would you like?", min_value=0, max_value=10, value=2)

st.markdown("---")

# 4. generate pssword
if st.button("🚀 Generate Password"):

    password_list = []

    #
    for _ in range(0, nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(0, nr_symbols):
        password_list.append(random.choice(symbols))  # 👈 symbols
    for _ in range(0, nr_numbers):
        password_list.append(random.choice(numbers))  # 👈 numbers

    # shuffle char
    random.shuffle(password_list)

    # join char
    password = "".join(password_list)

    # 5. print result
    st.write("### 🔑 Your Secure Password")
    # st.code : easy for copy
    st.code(password)

    st.success("Copy the password above and use it safely!")
    st.balloons()  # 🎈