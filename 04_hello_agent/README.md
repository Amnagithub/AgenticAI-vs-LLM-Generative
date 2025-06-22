# 🌟 OpenAI Agents using Google Gemini Model

🔗 **Useful Links:**
- [OpenAI Agents Docs](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents Model Configs](https://openai.github.io/openai-agents-python/models/)
- [Google Gemini API (OpenAI Compatible)](https://ai.google.dev/gemini-api/docs/openai)

---

## 🤖 Gemini Model Overview

- ✅ **Gemini** is a powerful model provided by Google.
- 🔐 **Base URL:** Required when connecting via OpenAI-compatible SDKs.
- ⚙️ Works seamlessly with the OpenAI Agents SDK.

---

## 🔑 Create Gemini API Key

👉 Get your Gemini API key by signing up at:

🌐 [Google AI Studio](https://aistudio.google.com/)

---

## 🛠️ Basic Agent with Gemini-API

1. `simpleAgent.py`  
   - 📌 Hands-on usage of Gemini API via an **agent-level** configuration.
   - ✅ Direct model interaction using `OpenAIChatCompletionsModel`.

2. `agentCLI.py`  
   - 💬 CLI-based agent conversation.
   - 🧠 Demonstrates **memory/state tracking** and persistent context.

---

## 🧠 How to Configure LLM Providers (OpenAI Alternatives)

### 1️⃣ Agent Level – Custom Logic per Agent

- Each agent has **its own LLM settings**.
- 🧩 Set model, key, base URL *inside the agent itself*.
- ✅ Ideal for **multi-agent workflows** where each agent has a unique role.

```python
agent = Agent(model=OpenAIChatCompletionsModel(...))


### 2️⃣ Runner Level – Default for All Agents

- The runner provides **global defaults** unless overridden.
- 🧩 Set model, key, base URL *inside the Runner*.
- ✅ Great for managing LLMs **across all agents** from a central place.

```python

Runner(model=OpenAIChatCompletionsModel(...))


### 3️⃣ Global Level – Project-wide Settings

- Set once (e.g., .env, config.yaml).
- 🧩 All agents and runners inherit this unless overridden.
- ✅ Best for small/simple projects.

```python
with function:

set_default_openai_api("chat_completions")
set_default_openai_client(client)