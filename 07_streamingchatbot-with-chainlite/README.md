# 🧠 Gemini-Powered Chainlit Assistant

This project is an interactive AI chatbot assistant built with Chainlit, using Gemini 2.5 via the OpenAI-compatible interface for real-time streaming responses.

## 🚀 Features

🌐 Gemini 2.5 Flash model integration via OpenAI-compatible API

💬 Real-time streaming of messages (token-by-token)

🔄 Persistent user session with context (agent, config, chat history)

🧵 Multi-turn conversation handling

⚙️ Clean structure with session management and logging

## 📁 Project Structure

```bash

├── main.py             # Main entry for Chainlit assistant
├── .env                # Store your GEMINI_API_KEY here
├── agents/             # Contains Agent and Runner logic
```

## 🧠 How It Works

Sets up the agent and stores it in session

On Message:

Retrieves previous chat history

Streams Gemini responses in real-time using Runner.run_streamed()

Updates the session with new conversation turns

### 🧑‍💻 Author

Built with ❤️ by [Amna Saif]
