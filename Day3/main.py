import streamlit as st

# 1. 아스키 아트와 환영 인사 크고 예쁘게 띄우기
st.title("🏝️ Treasure Island")

# 성벽 그림을 깨지지 않게 깔끔한 폰트로 출력
st.code('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/___/___/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

st.header("Welcome to Treasure Island!")
st.write("Your mission is to find the treasure. ✨")
st.markdown("---")

# 2. 첫 번째 선택: 갈림길 (라디오 버튼으로 깔끔하게 선택)
st.subheader("📍 You're at a cross road. Where do you want to go?")
chk_location = st.radio("Choose a direction:", ["Select...", "left", "right"], key="location")

if chk_location == "right":
    st.error("No, Jeffrey! I'm the right one :P. Try again!")

elif chk_location == "left":
    st.info("You've come to a lake. There is an island in the middle of the lake.")

    # 3. 두 번째 선택: 호수 (첫 번째를 통과해야만 등장!)
    st.subheader("🛶 What will you do?")
    chk_decision = st.radio("Choose an action:", ["Select...", "wait", "swim"], key="decision")

    if chk_decision == "swim":
        st.error("💥 No no no. You get attacked by an angry trout. Game Over.")
        st.snow()  # 눈 내리는 효과 (게임오버 썰렁함 연출)

    elif chk_decision == "wait":
        st.success("You arrive at the island unharmed. 👍")

        # 4. 세 번째 선택: 문 고르기 (두 번째까지 통과해야 등장!)
        st.subheader("🚪 There is a house with 3 doors. Which colour do you choose?")
        choice_door = st.radio("Choose a door colour:", ["Select...", "pink", "yellow", "blue"], key="door")

        if choice_door == "pink":
            st.balloons()  # 축하 풍선 펑펑!
            st.success("### 🎉 You found the treasure! You Win!")
            st.success("### ❤️ You will get a prize when you get back home!!!")

        elif choice_door == "yellow":
            st.error("🦁 You enter a room of beasts. Game Over.")
            st.snow()

        elif choice_door == "blue":
            st.error("🔥 It's a room full of fire!!! Game Over.")
            st.snow()