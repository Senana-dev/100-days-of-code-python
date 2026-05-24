import streamlit as st
import random
import sys
import os

# 🔥 file path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from hangman_art import stages, logo
from hangman_words import word_list

# 1. title and logo
st.title("🪓 Hangman Game")
st.subheader("Save the man, Jeffrey! 🤠")

st.code(logo)
st.markdown("---")

# 2. 🌟 Streamlit Session State

if "chosen_word" not in st.session_state:
    st.session_state["chosen_word"] = random.choice(word_list)
    st.session_state["lives"] = 6
    st.session_state["correct_letters"] = []
    st.session_state["game_over"] = False

# mapping variables
chosen_word = st.session_state["chosen_word"]
lives = st.session_state["lives"]
correct_letters = st.session_state["correct_letters"]
game_over = st.session_state["game_over"]

# st.write(f"(Secret for dev: {chosen_word})")

# 3. Status Display
display = ""
for letter in chosen_word:
    if letter in correct_letters:
        display += letter + " "
    else:
        display += "_ "

st.write("### Word to guess:")
st.markdown(f"## `{display.strip()}`")

# 4. current life with hangman
st.write(f"### 🛑 Lives Left: {lives} / 6")
st.code(stages[lives])

st.markdown("---")

# 5. input is working exclude game over.
if not game_over:
    # input chars set.
    guess = st.text_input("Guess a letter:", max_chars=1).lower()

    if st.button("Submit Guess 🎯"):
        if guess == "":
            st.warning("Please type a letter first!")
        elif guess in correct_letters:
            st.warning(f"You've already guessed '{guess}'")
        else:
            # correct new chars.
            if guess in chosen_word:
                correct_letters.append(guess)
                st.session_state["correct_letters"] = correct_letters
                st.success(f"Good job! '{guess}' is in the word!")
            # wrong
            else:
                lives -= 1
                st.session_state["lives"] = lives
                st.error(f"You guessed '{guess}', that's not in the word. You lose a life. 😢")

            # rerun...
            st.rerun()

# 6. 승패 판정 및 리셋 기능
# 단어에 빈칸이 없고 다 맞췄을 때
if "_" not in display:
    st.session_state["game_over"] = True
    st.balloons()  # 이기면 축하 풍선 펑펑!
    st.success("🎉 YOU WIN! You saved the hangman!")

# 목숨을 다 잃었을 때
if lives <= 0:
    st.session_state["game_over"] = True
    st.snow()  # 지면 차가운 눈 스르륵...
    st.error(f"☠️ GAME OVER! The word was: **{chosen_word.upper()}**")

# 게임이 끝났을 때만 나타나는 깔끔한 리셋 버튼
if st.session_state["game_over"]:
    if st.button("🔄 Play Again"):
        # 모든 내부 기억장치를 삭제하여 완벽하게 리셋
        st.session_state.clear()
        st.rerun()