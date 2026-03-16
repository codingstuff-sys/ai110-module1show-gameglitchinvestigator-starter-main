# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran the game it felt messy - the hints were lying, the secret number kept changing, and the New Game button didn’t seem to actually reset the UI. Two clear bugs were that the hints were backwards (it told me to go higher when I should go lower) and the secret/state wasn't stable across interactions. It mostly looked like the app was re-running and regenerating values at the wrong times.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used Copilot as my AI helper. It gave a good suggestion to fix the higher/lower logic, which I verified by replaying the game and watching the hints match the secret. One annoying thing was it sometimes pushed for big rewrites when I only wanted small fixes, so I had to steer it back to focused changes.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when I could reproduce the bad behavior, make the change, and then rerun the app and the problem was gone. I ran a manual play session (using Developer Debug Info) and a pytest that checks hint logic — both showed the hints are now correct. Copilot helped sketch the tests and the assertions, but I still ran and reviewed them myself.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because Streamlit re-runs the whole script on user interactions, and the original code regenerated the secret on each rerun instead of preserving it. I explain reruns like a reactive refresh: the script is executed again when widgets change, so you use `st.session_state` to hold values that must persist between runs. To fix it I only set the secret once in `st.session_state` (unless the player hits New Game), and I added a proper New Game handler that resets state intentionally.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I’ll keep is writing small, focused unit tests and running them after each change, plus committing often so I can roll back easily. Next time I work with AI I'll be more specific with prompts and ask for small, incremental edits instead of big rewrites, and I'll verify every suggestion with tests. This project showed me that AI is great for speeding things up, but its output still needs human review and tests before you trust it.
