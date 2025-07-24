import streamlit as st

SUGGESTIONS = [
    "What are your high-protein options?",
    "Show me gluten-free meals",
    "Recommend low-calorie bowls",
    "What’s the best vegan dish?"
]

def launch_chat_ui(chat_engine):
    st.set_page_config(page_title="Signature Cafe Assistant", page_icon="🥗")
    st.title("👋 Hi, I’m Yara — your personal Signature Cafe assistant!")
    st.markdown(
        "_Ask me anything about our delicious and healthy Mediterranean menu — I’m here to help you eat well!_ 🍽️🥗"
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.show_suggestions = True
        st.session_state.pending_suggestion = None

    # === Handle pending suggestion after rerun ===
    if st.session_state.pending_suggestion:
        question = st.session_state.pending_suggestion
        st.session_state.pending_suggestion = None

        # Avoid duplicate processing
        if not any(m["role"] == "user" and m["content"] == question for m in st.session_state.messages):
            st.session_state.messages.append({"role": "user", "content": question})

            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):
                thinking = st.empty()
                thinking.markdown("🌿 Let me find the best options for you...")
                response = chat_engine.chat(question)
                thinking.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.show_suggestions = False

        st.rerun()

    # === Show message history ===
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # === Suggestion buttons (first interaction only) ===
    if st.session_state.show_suggestions and st.session_state.pending_suggestion is None:
        st.info("Need inspiration? Try one of these:")
        cols = st.columns(len(SUGGESTIONS))
        for i, suggestion in enumerate(SUGGESTIONS):
            if cols[i].button(suggestion, key=f"suggestion_{i}"):
                st.session_state.pending_suggestion = suggestion
                st.rerun()

    # === Chat input at bottom ===
    prompt = st.chat_input("What would you like to know about our menu today?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            thinking = st.empty()
            thinking.markdown("🌿 Let me find the best options for you...")
            response = chat_engine.chat(prompt)
            thinking.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
