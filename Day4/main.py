import streamlit as st
import random

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
    key="user_rps",
    index=0
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
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3end5MG00OXBwc2d3eTBsanlraGRtNGdzaTcxeGpqejg2NnR6N3Y0cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fXnRObM8Q0RkOmR5nf/giphy.gif", use_container_width=True)
    elif your_choice < my_choice:
        st.error("😭 You lose! Better luck next time.")
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ejBla2VqZW5jNjl4Nm80N3oxcW4wYmZwdm90YmJraTk4OHhrYmI2ciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ZRcYyl26ZrahzWShDr/giphy.gif", use_container_width=True)
    elif your_choice > my_choice:
        st.success("🎉 You win! Awesome!")
        st.balloons()
    elif your_choice == my_choice:
        st.info("🤝 It's a draw! Play again.")