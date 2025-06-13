# 📡 What is OpenRouter?

OpenRouter is a platform that allows developers to **create**, **train**, and **deploy AI models** with ease. It supports OpenAI's Chat Completion API along with 200+ other models, making it ideal for building chatbots, virtual assistants, and intelligent AI applications.

---

## 🧭 User Interface and API

OpenRouter offers:

- ✅ A **User Interface**: Includes a chatroom to test models, manage accounts, track token usage, and view billing.
- ✅ A **Developer API**: Allows integration with applications via a standard OpenAI-compatible interface.

---

## 🛠️ Support for Function Calling

OpenRouter **supports function calling (tool use)**. This allows AI models to decide when and how to call external tools (e.g., weather APIs or calculators), making agents more useful in real-world applications.

---

## 🌐 Hosted vs Proxy

OpenRouter works as a **proxy**, routing your API requests to third-party model providers. It doesn't host models itself but enables access to **over 200+ models** by handling:

- Authentication
- Rate limiting
- Model translation

---

## 🤖 Using OpenRouter with OpenAI Agents SDK

## ✅ Prerequisites

1. 🔐 **Sign up** at [OpenRouter](https://openrouter.ai)
2. 🧪 **Get your API key**
3. 🆓 **Choose a free model** (e.g., `deepseek-chat-v3-0324:free`)

### Free & Paid Models

OpenRouter supports both **free** and **paid** models. You can find the full list here:  
📄 [https://openrouter.ai/models](https://openrouter.ai/models)

---

## ⚙️ Installation

### 📦 Install OpenAI Agents

```bash
pip install openai-agents

Install OpenAI Agents Dep.

```bash

pip install -Uq openai-agents
