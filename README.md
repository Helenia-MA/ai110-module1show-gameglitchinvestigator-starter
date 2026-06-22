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
The purpose of the game is for the player to guess a number within a given range based on the difficulty level before the allowed attempts are over. One can opt to get hints notifying them whether their guess is too high or too low and the game ends when one guesses correctly or the attempts are depleted
- [ ] Detail which bugs you found.
The hint messages were inversed, showing 'go lower' when the guess was lower than the correct value and vice versa.

after winning/losing a game the 'New game', only the developer bug info is updated while the rest of the game stays stuck on the end of the previous game

The range of numbers to choose from was larger for 'diffcult' level comapred to 'Normal'

The game started with attempt already equal to 1 instead of 0
- [ ] Explain what fixes you applied.

Corrected the hint messages to show the correct error ie when the guess was higher it returned 'Too high' and when it was lower it returned 'too low' as expected

updated the new game session state for status to "playing" in order for the logic to update to playing mode and allow for a new game to start after the end of the previous one

switched the ranges making the range for 'difficult' level 1-100 and for 'Normal': 1-50

updated the initialized value for score for a new game to 0 instead of 1

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

Correct guess is '43'
1. User enters a guess of 40
2. Game returns "Too Low"
3. User enters a guess of '70' -> "Too High"
4. Score updates correctly after each guess (-5 for each wrong guess)
5. Attempts left updates correctly for each guess
6. User enters a guess of 43
7. Game ends after the correct guess
8. User clicks 'New Game' button
9. Game resets the session state: new secret value, attempts: 0, score: 0, the appropriate difficulty level and an empty history list

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

tests/test_game_logic.py ......................  [100%]

================== 22 passed in 0.05s ==================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
