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

- [ ] Describe the game's purpose.
A simple number-guessing game built with Streamlit. The player tries to guess a secret integer in a difficulty-dependent range, gets higher/lower hints, and has a limited number of attempts to score points.
- [ ] Detail which bugs you found.
   - Hints were reversed (the app told players to "go higher" when the guess was already higher than the secret).
   - The secret number kept changing across interactions because it was being regenerated on reruns instead of stored in session state.    - Pressing "New Game" didn't consistently reset the visible UI/state (attempts, history, input), so a new game felt incomplete.
   - There was a type mismatch edge case where the secret was sometimes a string, breaking numeric comparisons.
- [ ] Explain what fixes you applied.
   - Fixed the hint logic by normalizing secret values and returning the correct higher/lower messages.
   - Stored the secret (and other persistent values) in `st.session_state` so it survives Streamlit reruns.
   - Implemented a proper New Game handler that resets secret, attempts, score, history and clears the input, then triggers a rerun so the UI updates.
   - Refactored core game logic into `logic_utils.py` and added pytest unit tests (including a regression test for the string-secret case).
   - Added short inline comments noting where AI-assisted edits happened to make changes traceable.



## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
- [ ] 

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
