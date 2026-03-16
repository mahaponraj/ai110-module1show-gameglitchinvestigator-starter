# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**  
  The game is a number-guessing app built with Streamlit where players guess a secret number within a range based on difficulty (Easy: 1-20, Normal: 1-100, Hard: 1-50). It provides hints ("Go Higher" or "Go Lower"), tracks attempts and score, and ends when the player wins or runs out of attempts. The goal is to guess correctly in as few attempts as possible for a higher score.

- [x] **Detail which bugs you found.**  
  1. **Incorrect Hints**: The hint messages were backwards—"Too High" said "Go HIGHER!" (should be "Go LOWER!") and "Too Low" said "Go LOWER!" (should be "Go HIGHER!").  
  2. **New Game Button Failure**: Clicking "New Game" showed "Game over, start a new game" instead of resetting, because it didn't clear the game status ("won" or "lost") from session state.  
  3. **Unstable Secret Number**: The secret number changed unpredictably due to Streamlit's reactive reruns, as it wasn't persisted in session state.

- [x] **Explain what fixes you applied.**  
  1. **Fixed Hints**: Swapped the message text in `check_guess()` so "Too High" now says "📉 Go LOWER!" and "Too Low" says "📈 Go HIGHER!".  
  2. **Fixed New Game**: Added `st.session_state.status = "playing"` in the new_game button handler to reset the game state properly.  
  3. **Stabilized Secret**: Ensured the secret is generated only once per game using `if "secret" not in st.session_state` and updated the new_game button to use the correct difficulty range instead of hardcoded 1-100.  
  Additionally, refactored logic functions to `logic_utils.py` for better organization and added comprehensive tests (30 passing) to prevent regressions.

## 📸 Demo

- [x] Hint shows "Go Higher" for low guesses  
 ![Hints "Go Higher"](image-4.png)

- [x] Hint shows "Go Lower" for high guesses  
 ![Hints "Go Lower"](image-5.png)

- [x] Game ends when attempts reach 0  
![Game Over When Attempts are 0](image-6.png)

- [x] Winning screen appears correctly  
![Won The Game!](image-2.png)

- [x] New Game button resets the game  
![Restarts Game After Clicking New Game Button](image-3.png)

- [x] Pytest results passing  
![Test Runs](image-1.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
