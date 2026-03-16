# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
An ai suggestion that was correct was when it corrrectly edited the logic of when to say" go higher" or "go lower", and i verified this by replaying the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The ai was suggesting to completley replace all the code to make a better and improved game, so it was misleading in what I wanted it to do. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
When I reran the game, and tested what was broken the first time.
- Describe at least one test you ran (manual or using pytest)    and what it showed you about your code.
I ran a test to see if the "go higher" "go lower" hints worked, and it showed that it did work.
- Did AI help you design or understand any tests? How?
AI did help design the pytests, which it ran itself, and helped fix logic.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  The secret number kept changing because Streamlit re-executes the script on many user interactions. In the original version the secret was being re-created on reruns instead of being kept session storage, so the number changed unexpectedly.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit works by re-running your whole Python script whenever the user interacts with the UI; think of it like a reactive page refresh. Reruns basically just means the code is being re-executed and session state is what's stored in a space(like variables) between these re-executions.

- What change did you make that finally gave the game a stable secret number?

  I fixed the issue by storing the secret number in `st.session_state` and only setting it when the session doesn't already have a secret (i.e., `if "secret" not in st.session_state: st.session_state.secret = random.randint(low, high)`). I also implemented a proper New Game handler that resets `st.session_state.secret` (and other state like attempts and history) when the user presses the New Game button, then triggers a rerun so the UI reflects the reset. That combination produced a stable secret number during normal play while still allowing a controlled reset when the player requested a new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  Write small, focused unit tests and run them after each change; commit frequently with clear messages.

- What is one thing you would do differently next time you work with AI on a coding task?

  Give the AI narrow, specific prompts and request small, incremental edits instead of full rewrites; always verify suggestions with tests.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI is a fast, helpful coding teammate for prototyping, but its output should be treated as a draft: verify with tests and human review before trusting it.
