import streamlit as st
from llm_handler import get_available_models, generate_response
from utils import load_prompt_examples

st.set_page_config(page_title="LLM Chatbot", layout="wide")



st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("---")

st.title("🤖 LLM Chatbot with Your API Key")



# Sidebar for API Key Input and Model Selection
st.sidebar.header("🔐 API Key & Model Selection")

api_key = st.sidebar.text_input("Enter your API Key", type="password")
provider = st.sidebar.selectbox("Choose Provider", ["OpenAI", "OpenRouter", "HuggingFace"])

base_url = ""
if provider == "OpenRouter":
    base_url = st.sidebar.text_input("API Base URL", value="https://openrouter.ai/api/v1/chat/completions")
elif provider == "HuggingFace":
    base_url = st.sidebar.text_input("API Base URL", value="https://api-inference.huggingface.co/models/")

st.session_state['base_url'] = base_url

# Load Models after API Key is entered
if api_key:
    models = get_available_models(provider)
    selected_model = st.sidebar.selectbox("Select Model", models)

    custom_model = st.sidebar.text_input("Or enter a custom model name (optional)")
    if custom_model.strip():
        selected_model = custom_model.strip()

    # Tabs
    tab1, tab2, tab3 = st.tabs(["💬 Chat", "📘 Prompt Guide", "📤 Export / History"])

    with tab1:
        # Chat logic (same as before)
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        st.markdown("### 💬 Chat")

        chat_container = st.container()
        with chat_container:
            for idx, (sender, message) in enumerate(st.session_state.chat_history):
                with st.chat_message(sender):
                    st.markdown(message)
                    if sender == "Bot":
                        st.code(message, language='markdown')
                        st.markdown(
                            f"""<button onclick="navigator.clipboard.writeText(`{message}`)">📋 Copy</button>""",
                            unsafe_allow_html=True
                        )

        st.markdown("---")
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_area("You:", height=100, key="input", label_visibility="collapsed", placeholder="Ask something...")
        with col2:
            st.write("")
            st.write("")
            send_clicked = st.button("Send", use_container_width=True)

        if send_clicked and user_input.strip():
            with st.spinner("Generating response..."):
                reply = generate_response(
                    api_key,
                    selected_model,
                    user_input,
                    provider,
                    base_url=st.session_state.get('base_url')
                )
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Bot", reply))
            st.rerun()

    with tab2:
        st.markdown("## 📘 Prompt Engineering Guide")
        for label, prompt in load_prompt_examples().items():
            st.markdown(f"**{label}**")
            st.code(prompt)

    with tab3:
        st.markdown("## 📤 Export or Manage History")
        colA, colB, colC = st.columns(3)
        with colA:
            if st.button("🗑️ Clear Chat History"):
                st.session_state.chat_history = []
                st.rerun()
        with colB:
            if st.download_button("📄 Export as Markdown", data="\n\n".join(
                [f"**{sender}:** {message}" for sender, message in st.session_state.chat_history]),
                file_name="chat_history.md", mime="text/markdown"):
                st.toast("Chat exported as Markdown!")

        with colC:
            if st.download_button("📁 Export as JSON", data=str(st.session_state.chat_history),
                                  file_name="chat_history.json", mime="application/json"):
                st.toast("Chat exported as JSON!")


if not api_key:
    with st.container():
        st.markdown("### 👋 Welcome to the LLM Chatbot!")
        st.info("""
        ### 🧠 What is this?

        This is an **AI-powered chatbot interface** that lets you interact with large language models (LLMs) like ChatGPT, Claude, and Mistral — all from one simple web app.

        You can:
        - Ask questions
        - Get code explained
        - Write content or emails
        - Chat with different AI models using your own API keys

        ---

        ### 🚀 How to Get Started:

        1. **Enter your API Key** in the sidebar (don't worry, we don't store it).
        2. **Select a Provider** like OpenAI, OpenRouter, or HuggingFace.
        3. **Choose a model** (or paste your own custom model name).
        4. **Start chatting** at the bottom input bar — your responses will appear above.

        ---

        ### 🌐 Supported AI Providers:

        - 🔷 **OpenAI**  
        Models like: `gpt-3.5-turbo`, `gpt-4`  
        ➤ [Get your API key](https://platform.openai.com/account/api-keys)

        - 🔶 **OpenRouter**  
        Aggregates models like: `openai/gpt-4`, `anthropic/claude-3-opus`, `mistralai/mixtral-8x7b`  
        ➤ [Get your API key](https://openrouter.ai)

        - 🟡 **Hugging Face**  
        Community-hosted open-source models like: `mistralai/Mistral-7B-Instruct`  
        ➤ [Get your token](https://huggingface.co/settings/tokens)

        ---

        ### 🛡️ Your Privacy

        > ✅ Your API key is **never stored or shared**.  
        > ✅ All requests are sent securely from your browser session.

        ---

        💡 Need inspiration? Use the **📘 Prompt Guide tab** for pre-built examples.
        """)

