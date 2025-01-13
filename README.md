# GenZBot: Your Gateway to AI Chatbot Creation! 🤖✨

Welcome to **GenZBot**, the ultimate package designed to help beginners build AI chatbots from scratch. Whether you're just stepping into the world of Generative AI or looking to understand chatbot integration, GenZBot has got you covered! 🚀

---

## Features 🌟

- **Easy Setup**: Create an AI chatbot project structure with a single command.
- **Multiple LLMs**: Choose from 5 powerful language models:
  - `openai` 🔑 (requires a paid API key from OpenAI)
  - `gemini` 🌌 (free API key from Google AI Studio)
  - `gemma` 🧠  (all these other three have free API key from Groq)
  - `llama` 🦙
  - `mixtral` 🌀
- **Customizable Templates**: Two designs available:
  - `Plain` ✨
  - `Galaxy` 🌠
- **Personalization**: Set your bot's behavior and name easily.
- **Automated Environment Setup**: Virtual environment creation, dependency installation, and app execution are just one command away.

---

## Installation 🛠️

1. Install GenZBot using pip:
   ```bash
   pip install GenZBot
   ```

2. Import the `ChatBot` class:
   ```python
   from GenZBot.chatbot import ChatBot
   ```

---

## Getting Started 🚀

Here’s how to create your first chatbot project with GenZBot:

1. **Initialize Your ChatBot**:
   ```python
   bot = ChatBot(llm='gemini', api_key='your-api-key')
   ```

2. **Create Project Structure**:
   ```python
   bot.CreateProject()
   ```
   This command will generate the following structure:
   ```
   Chatbot_Project/
       AI_Service/
           AIResponse.py
       Backend/
           app.py
       Frontend/
           static/
               static.js
               style.css
           templates/
               index.html
       .env
       requirements
   ```

3. **Run the ChatBot**:
   ```python
   bot.run()
   ```
   This command will:
   - Create a virtual environment.
   - Install all dependencies from `requirements`.
   - Launch the Flask app.

---

## Example Code 📝

```python
from GenZBot.chatbot import ChatBot

# Step 1: Initialize ChatBot
bot = ChatBot(llm='gemini', api_key='your-api-key')

# Step 2: Create Project Structure
bot.CreateProject()

# Step 3: Run the Bot
bot.run()
```

---

## API Keys 🔑

- **OpenAI**: Obtain a paid API key from [OpenAI](https://openai.com/).
- **Gemini**: Get a free API key from [Google AI Studio](https://ai.google/).
- **Gemma, Llama, Mixtral**: Request API keys from [Groq AI](https://groq.com/).

---

## Why Choose GenZBot? 🤔

- Ideal for **beginners** looking to explore Generative AI.
- Provides a **clear project structure** for understanding AI chatbot integration.
- Saves time with **automated setup** and environment configuration.

---

## Demo


https://github.com/user-attachments/assets/5d2e1ce8-5fe2-4b1b-95ce-9b1e06ba2840


Happy Chatbot Building! 🎉
