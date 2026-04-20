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



   