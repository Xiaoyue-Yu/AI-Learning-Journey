# Prompt Engineeering

This section contains my study notes for *"ChatGPT Prompt Engineering for Developers".* https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/information

## 1. LLMs

* Base LLM

  Predicts next word, based on text training data

* Instruction Tuned LLM
  
  Tries to follow instructions

  Training tecnique: RLHF (Reinforcement Learing with Human Feedback)
  to make the system better able to be helpful and follow instructions.

## 2. Principles

* Write clear and specific instructions
  * Use delimiters
  * Ask for structured output
  * Check whether conditions are satisfied: Check assumptions required to do the task
  * Few-shot prompting: Give successful examples of completing tasks

* Give the model time to think
  * Specify the steps to complete the task
  * Instruct the medel to work out its own solution before rushing to a conclusion

## 3. Model Limitations
* Hallucination: Makes statements that sound plausible but are not true
  * How to reduce: First find relevant information, then answer the question based on the relevant information

## 4. Iterative Prompt Development
* Prompt Guidelines
  * Be clear and specific
  * Analyze why result does not give desired output
  * Refine the idea and the prompt
  * Repeat

* Iterative Process
  * Try something
  * Analyze where the result does not give what you want
  * Clarify instructions, give more time to think
  * Refine prompts with a batch examples

## 5. Summarizing (总结)
* Facilitates the organization of user comments within apps or websites -> Reducing reading time and better for data analysis

## 6. Inferring (推理)
By using prompts, we can rapidly construct inferences regarding complex natural language.

* Extract emotion/topic information
* Generate output in a more robust JSON format

## 7. Transforming
Use LLM to translate, do tones / formats transformation, and spell and grammar checking.

## 8. Expanding
Expand a shorter text to a longer text (email, essay).

* Parameter: temperature
  * randomness of the model.
  * temperature is higher means more random response.
  * If we want to build a system **more reliable and predictable**: use temp = 0; **more creative and require variety**: use temp > 0

## 9. Chatbots
* Message
  * User message: input
  * Assistant message: output
  * System message: sets behavior of assistant







   