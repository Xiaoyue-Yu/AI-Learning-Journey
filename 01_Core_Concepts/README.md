# Core Concepts
[EN](./README.md) | [中文](./AI_Concepts_zh.md)

## The Foundations

### 1. AI (Artificial Intelligence)

AI is a field of science and technology focused on enabling machines to simulate human intelligence.
Its goal is to build systems that can perform tasks that typically require human intelligence, such as:
- understanding and generating language
- recognizing images and speech
- making judgments and decisions
- learning from data and continuously improving performance

By capability scope, AI is commonly divided into two core concepts:

#### 1.1. ANI (Artificial Narrow Intelligence)

ANI is **Artificial Narrow Intelligence**, also known as "weak AI."
It performs very well on specific tasks but cannot generalize across domains.

Common examples:
- recommendation systems (e.g., short-video recommendations)
- single-purpose voice assistant functions
- face recognition
- board-game playing programs

#### 1.2. AGI (Artificial General Intelligence)

AGI is **Artificial General Intelligence**, also known as "strong AI."
It refers to a system with broad, human-like intelligence that can reason, learn, and transfer knowledge across many domains.

AGI remains a research goal and has not been fully achieved yet.


### 2. ML (Machine Learning)

Machine Learning is a **subset** of Artificial Intelligence focused on building systems that learn from data. Instead of being explicitly programmed with rigid rules to perform a task, ML algorithms use statistical models to identify patterns within large datasets, allowing the system to automatically improve its performance and make predictions over time.

Relationship between AI and ML: AI is the **goal**, ML is the **method**.

#### 2.1. Supervised Learning
- Input(A) -> Output(B) (Input to Output mapping)
- Highly relies on **labeled data quality/quantity** and **model capacity**.

#### 2.2. Unsupervised Learning
- Learns structure from unlabeled data.
- Common tasks include clustering, dimensionality reduction, and anomaly detection.

#### 2.3. Reinforcement Learning
- An agent interacts with an environment and learns through rewards and penalties.
- Common in game-playing, robotics, and sequential decision-making.


### 3. DL (Deep Learning)

Deep Learning is a **subset** of Machine Learning based on multi-layer neural networks.

#### 3.1. Why Deep Learning Matters
- It can automatically learn high-level representations from raw data.
- It drives major advances in computer vision, speech recognition, and natural language processing.

#### 3.2. Connection to Modern AI
- Most modern LLMs are built with deep learning architectures (for example, Transformers).
- In practice: AI is the broad field, ML is a core approach, and DL powers many state-of-the-art AI systems.


## The GenAI Era (生成式 AI 与 LLM)

### 4. GenAI & LLMs (Generative AI & Large Language Models)

Deep Learning is the foundation, but Generative AI is the breakthrough that brought AI into everyday life. 

#### 4.1. Generative AI (GenAI)
Unlike traditional ML which classifies or predicts (e.g., "Is this a cat?"), GenAI creates **net-new content**—text, images, audio, or video—based on patterns learned from training data.

#### 4.2. LLM (Large Language Model)
An LLM is a specific type of GenAI focused entirely on text. 
- **Core Mechanism:** At its lowest level, an LLM simply predicts the next most likely token (word/character) based on the context of the prompt.
- **Architecture:** Most modern LLMs are built on the **Transformer** architecture (a specific Deep Learning model).
- **Examples:** GPT-5, Gemini 3 Pro.

##### 4.2.1 Tokens (What the model actually reads)
An LLM doesn't really “read” words. It reads **tokens**, which are small text units produced by tokenization.  
A token can be a whole word, part of a word, or even punctuation.

Tokenization converts your input into a sequence of token IDs; the model then processes these tokens and generates the next token step by step.

Two practical consequences:
- The **context window** is measured in tokens, so very long prompts may get truncated.
- Different tokenizers count tokens differently, so token limits and costs depend on the specific model.

Try tokenizer: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)  
<img src="./01_pics/01_token.jpg" alt="OpenAI tokenizer example" style="max-width: 100%;" />

#### 4.3. Practical Limitation
- LLMs can sound confident while being wrong ("hallucination"), so output still needs verification for critical tasks.


## Agents & Engineering

### 5. AI Agents & Skills

If an LLM is just a "brain in a jar" that only talks, an AI Agent is that same brain equipped with hands, eyes, and memory.

#### 5.1. AI Agent
An AI Agent is an autonomous system driven by an LLM that can perceive its environment, make decisions, and take actions to achieve a specific goal. 
The standard formula for an Agent is: **Agent = LLM + Memory + Planning + Tools**.

#### 5.2. Skills / Tools
Skills (or Tools) are the "hands" of the Agent. Because an LLM alone cannot calculate math accurately or browse today's news, we give it APIs (interfaces) to call. 
Reference video: [《【闪客】一口气拆穿Skill/MCP/RAG/Agent/OpenClaw底层逻辑》](https://www.bilibili.com/video/BV1ojfDBSEPv?vd_source=7ec1163e22daf4515c09a5b6d9b99bae)  
<img src="./01_agent/01_agent.jpg" alt="Skill/MCP/RAG/Agent/OpenClaw explainer" style="max-width: 100%;" />

##### 5.2.1 Context Prompts
LLMs don’t just answer from their weights; they rely heavily on the context you provide. A context prompt is the set of messages plus retrieved information that gives the model the background it needs.

Common context sources include:
- system instructions (behavior + rules)
- user request (the actual goal)
- retrieved documents (RAG results), logs, database snippets, or tool outputs

Because the context window is limited, good prompting is often about selecting the most relevant pieces, not dumping everything.

##### 5.2.2 MCP (Model Context Protocol)
MCP (Model Context Protocol) is a protocol that helps models and agents connect to external tools, resources, and data in a standardized way.

In practice, MCP reduces “one-off integrations” by making context acquisition and tool access more consistent:
- agents can discover available resources and actions
- tool calls can follow a common interface
- applications can expose only what is safe/needed

For an Agent workflow, MCP acts like a reliable bridge between the LLM and the outside world.

- **Examples:** Web Search Skill, Python Execution Skill, Database Query Skill. 
- **Workflow:** You ask the Agent for today's weather -> It plans the steps -> It uses the "Web Search Skill" -> It feeds the result back to the LLM -> The LLM formulates a human-readable answer.

### 6. AI-Driven Development (The "Vibe Coding" Era)

Applying LLMs and Agents to software engineering has created a new paradigm often colloquially called **"Vibe Coding"**—where developers steer the architecture using natural language (prompts) while AI coding agents handle the syntax.

#### 6.1. Cursor
- **What it is:** An AI-first code editor (a fork of VS Code).
- **Best for:** Human-in-the-loop pair programming. It features a powerful GUI, excellent codebase context understanding, and real-time diff previews.

#### 6.2. Claude Code
- **What it is:** A CLI (Command Line Interface) agent developed by Anthropic.
- **Best for:** Terminal-native workflows. It acts autonomously to navigate your directories, run tests, and refactor code directly from your terminal, without a graphical interface.

#### 6.3. OpenAI Codex
- **What it is:** A comprehensive Agentic Coding platform by OpenAI. 
- **Best for:** Delegating complex, multi-threaded tasks. It can manage its own Git worktrees, run parallel development threads, and act more like an autonomous virtual development team rather than just an autocomplete assistant.