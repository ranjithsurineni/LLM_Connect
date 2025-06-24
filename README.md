# 🤖 Multi-Provider LLM Chatbot

A **Streamlit-based conversational AI application** designed to interface with leading large language model (LLM) APIs including **OpenAI**, **OpenRouter**, and **Hugging Face**. This application allows users to securely plug in their own API keys, select models dynamically, and engage in rich, contextual chatbot conversations — all through a seamless, privacy-conscious interface.

---

## 🚀 Features

- ✅ **Supports multiple AI providers** (OpenAI, OpenRouter, Hugging Face)
- 🔐 **API-key protected**, no backend storage, secure session-based access
- 🧠 **Prompt Engineering Guide** tab with reusable examples
- 💬 Real-time chatbot experience with sticky chat input
- 📤 **Export chat history** (Markdown / JSON)
- 📋 **Copy-to-clipboard** for AI responses
- 🧹 **Clear chat history** option
- 🧩 Modular code structure for easy integration & extension

---

## 🌐 Supported Providers & Models

| Provider | Example Models | Get API Key |
|---------|----------------|-------------|
| **OpenAI** | `gpt-3.5-turbo`, `gpt-4` | [🔗 openai.com](https://platform.openai.com/account/api-keys) |
| **OpenRouter** | `anthropic/claude-3-opus`, `mistralai/mixtral-8x7b` | [🔗 openrouter.ai](https://openrouter.ai) |
| **Hugging Face** | `mistralai/Mistral-7B-Instruct`, `tiiuae/falcon-7b` | [🔗 huggingface.co](https://huggingface.co/settings/tokens) |

---

## 🛠️ How It Works

1. User enters their API key from any supported provider in the sidebar.
2. The model list is dynamically shown or a custom model can be manually entered.
3. User types messages in a fixed input box at the bottom of the screen.
4. The chat history appears above in a live conversation layout.
5. Users can export chat logs, clear them, or copy individual responses.

---

## 💡 Prompt Guide Included

The app includes a **Prompt Engineering tab** with curated templates for:
- Writing help
- Code generation
- Content summarization
- Use-case specific guidance

---

## 🔒 Security & Privacy

- No API keys or inputs are logged or stored.
- All interactions are contained in the browser session.
- Built using **Streamlit** for UI simplicity and transparency.

---

## 📁 Folder Structure

```bash
├── app.py                  # Main Streamlit UI
├── llm_handler.py          # LLM abstraction logic (OpenAI, OpenRouter, HuggingFace)
├── utils.py                # Prompt templates and helpers
├── requirements.txt        # All required Python packages
└── README.md               # You’re here
```
---

##  📦 Installation & Setup

# Step 1: Clone the repo
```bash
git clone https://github.com/your-username/llm-chatbot-app.git
cd llm-chatbot-app
```

# Step 2: Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

# Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

# Step 4: Run the app
```bash
streamlit run app.py
```

----

## 📌 Why This Project Matters

This project demonstrates:

- Proficiency in working with LLMs, APIs, and frontend integration

- Design of provider-agnostic architecture (extendable to Cohere, Anthropic, etc.)

- Clean UI/UX using Streamlit with real-time interaction handling

- Readiness for enterprise applications in AI customer service, support bots, or developer assistants

---
## 👨‍💻 Built By

**Ranjith Kumar Surineni**  
_Data Scientist & AI Engineer_

- 🔗 [GitHub](https://github.com/ranjithsurineni)
- 💼 [LinkedIn](https://www.linkedin.com/in/ranjithsurineni)
- 📧 [Email](mailto:ranjithsurineni.official@gmail.com)


"Designed with scalability and production-readiness in mind — ready for deployment in B2B/B2C LLM tools and client solutions."
