import streamlit as st
import random
st.title("✊✌️✋Rock Paper Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Title and introducing.
st.title("✊✌️✋ Rock Paper Scissors")
st.subheader("Can you beat the computer, Jeffrey? 😉")
st.markdown("---")

# 3. User selection
st.write("### 👤 Your Choice")
choice_label = st.radio(
    "Choose one:",
    ["Select...", "Rock (0)", "Paper (1)", "Scissors (2)"],
    key="user_rps"
)

# It's working by user selection.
if choice_label != "Select...":
    if "Rock" in choice_label:
        your_choice = 0
    elif "Paper" in choice_label:
        your_choice = 1
    else:
        your_choice = 2

    # show images of user
    st.code(game_images[your_choice])

    st.markdown("---")

    # 4. Computer selection
    st.write("### 🤖 Computer's Choice")
    my_choice = random.randint(0, 2)
    st.code(game_images[my_choice])

    st.markdown("---")

    # 5. Result
    st.write("### 🏆 Result")

    if your_choice == 0 and my_choice == 2:
        st.success("🎉 You win! Perfect match!")
        st.balloons()  # ballons
    elif your_choice == 2 and my_choice == 0:
        st.error("😭 You lose! Better luck next time.")
        st.image("https://media.giphy.com/media/l0IxYWDltdHEqv9f2/giphy.gif", use_container_width=True)
    elif your_choice < my_choice:
        st.error("😭 You lose! Better luck next time.")
        st.image("https://media.giphy.com/media/l0IxYWDltdHEqv9f2/giphy.gif", use_container_width=True)
    elif your_choice > my_choice:
        st.success("🎉 You win! Awesome!")
        st.balloons()
    elif your_choice == my_choice:
        st.info("🤝 It's a draw! Play again.")

# 🔥 6. Game reset
    # Go back to select
    if st.button("🔄 Play Again (Reset Game)"):
        st.rerun()