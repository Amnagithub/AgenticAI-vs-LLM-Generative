# 🤖 Gemini-Powered Chat Agent with Chainlit

This project is a conversational AI chatbot built using **[Chainlit](https://docs.chainlit.io/)** and **Google Gemini API**. It leverages a custom agent framework with session management, dynamic message handling, and a structured conversation flow.

---

## 🧠 Features

- 💬 Interactive chatbot UI with **Chainlit**
- 🤝 Agent-based architecture powered by a custom **Runner + Agent**
- 🔁 Persistent chat history across user sessions
- 🔐 Loads Gemini API Key from `.env`
- ⚡ Uses **Gemini 2.0 Flash** model for fast responses
- 🧪 Clean logging and error handling

---

## 📦 Installation

```bash
uv init chatbot
cd chatbot
uv add openai-agents chainlit python-dotenv

```

## 🛠 How It Works

### On Chat Start

- Gemini model is initialized  
- Agent and chat history are saved in session  
- A welcome message is sent to the user  

### On Message

- Message is added to the history  
- Runner calls the agent with full history  
- Response is streamed back and shown  
- History is updated for the next turn  
