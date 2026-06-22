# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").

The normal difficulty level has a bigger range of numbers to guess from compared to hard level

The hints given are inverse i.e 'go lower' instead of 'go higher' and vice versa

after winning/losing a game the 'New game', only the developer bug info is updated while the rest of the game stays stuck on the end of the previous game

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.
1.
Input: Guessed 50 when the correct value was 53
Expected Behavior: hint; 'go higher'
Actual Behavior: hint; 'go lower'
Console/Output error: none

2.
Input: switched difficulty level from 'normal' to 'hard'
Expected Behavior: the range of numbers to guess from should increase
Actual Behavior: the range decreases from 1-100 to 1-50
Console/Output error: none

3.
Input: starting 'new game' after the end of the previous one
Expected Behavior: accepts submission and displays the appropriate hint or success message
Actual Behavior: only the 'Developer Debug Info' values are updated, the 'Submit Guess' button is unresponsive
Console/Output error: none


| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot, Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It helped in pinpointing that there was more than one logic causing the bug in the score value:
one was the parity logic that had been added although it didn't really make sense based on the logic of the game and the second was the winning score logic where the calculation used 'atempt + 1' instead of 'attempt - 1'.
It also helped in debugging the attempts logic bug since one of the score calculation logic as seen above, was dependent on it.
I verified the results by asking it to generate pytests and by confirming the logic worked correctly in the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
While refactoring the 'parse_guess' to logics_util.py, its suggestion included 'update_scores' and 'check_guess' logics also refactored without prior instructions to do so.
To work on them independently, i ignored the suggested changes and started a new chat with a more specific instruction on focusing solely on the requested logic

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I used claude to generate tests to confirm the 'New Game' logic and that all the required session info was correctly updated. One of the tests was in ensuring that the session state as updated to "playing" to allow for a new game to start upon clicking the 'New Game' button.
Claude suggested making a helper function for updating the new game state for easier testing and to also be able to more easily confirm all the information required was updated accordingly.



---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
for every interaction, streamlit reruns the entire code which means it resets regular variables to their initial values, so to ensure persistence, we use session state to store the values of variables we want to persist.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Handling the testing for each problem one at a time instead of all at the end.

- What is one thing you would do differently next time you work with AI on a coding task?
I would try writing more specific prompts on the first go to avoid having to repeat or need to add too much information as the chat progresses.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

It helped me realize that there are a lot more logic errors in AI generated material that can be easily overlooked if not properly scrutinized.
