# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The glitch game had a simple UI with deifficulty settings on the left. I liked that it didn't overwhelm with a lot of texts and instructions. I noticed "something is off" in the game website and played it. I felt there are lots of things to be addressed.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  a. The hints are absolutely incorrect (it kept saying to go higher till 99 and said lower in 100. Then it said the correct answer is 24). The hints should be correctly given to play the game
  
  b. I had an extra attempt left but it ended before that. It should've allowed me to do the last attempt to guess
  
  c. when i clicked "new game" it says "game over, start a new game" ie it doesnt start a new game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Github copilot in VS Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Mostly it guided me well and gave me fixes for the bugs like for example for restarting the game, it cleared helped me understand what was missing and few lines should be added for restarting the game, history attempts and array.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

It didn't actually know that the input box was using the previous game answer as the first one when the game restarted. So I had that issue where it didn't detect that but once I identified the problem and explained, it fixed that too.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I run the game and played it. I had to play it multiple times to visualize if the bug was fixed. Also pytests were helpful while fixing the bugs.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

a. test_update_score_win(): this test was written for verifing score calculation during each attempt. It shows the scoring formula ie 100-10*(attempts+1) with a minimum score of 10. thus it shows if the player answers correctly faster, he scores higher.

b. test_guess_too_low(): here the test checks if the guess is "too low" and if thats the case it hints to go higher. The hint logic is accurately refined and altered according to the secret number each game.

- Did AI help you design or understand any tests? How?

It helped me understand the edge cases that needs to be addressed while writing the tests.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

It was changing because the secret number was generated each tim,e the app rerun like clicking any button. Then it was fixed that the secret number should be same for the entire game for generating proper hints and maintaining attempt history

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would say that imagine whenever you use random website for watching movies and whenever you click somewhere it triggers and opens another tab for ads and spam so thats what happening here where the game secret number is triggered and updated each time I click some button on the game. So to prevent ads to be triggered we use ad blockers and here I just altered the code to make sure the secret number is not triggered to change unless new game is restarted 

- What change did you make that finally gave the game a stable secret number?

I wrapped the secret number generation in a session state check (if "secret" not in st.session_state) ensuring it created only once per game session and persists across Streamlit reruns.
This prevented the number from changing unpredictably with every button click or input. Additionally, I updated the "New Game" button to reset the secret using the selected difficulty range instead of hardcoding 1-100.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Giving appropriate prompts and tagging the code files will be incorporated in my habits. I'll have new chat for each bug which helped me focus on one thing at a time

- What is one thing you would do differently next time you work with AI on a coding task?

I'll write tests as soon as the bugs are fixed and test using that

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I was mindblown by the agent mode where it even helped me apply updated code to the file in the appropriate lines. It really did improve my productivity by 90% by initially understanding the code to get started.