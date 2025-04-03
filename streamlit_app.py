import streamlit as st
from chat_sql import ask_db

st.set_page_config(page_title="Chat with Azure SQL", layout="wide")

st.title("💬 Chat with Azure SQL Database")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask a question about your data...")

if user_input:
    with st.spinner("Thinking..."):
        result = ask_db(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": result})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        if isinstance(msg["content"], dict):
            if msg["content"].get("sql"):
                st.markdown(f"**🧠 SQL Query:**\n```sql\n{msg['content']['sql']}\n```")
            if msg["content"].get("explanation"):
                st.markdown(f"**ℹ️ Explanation:** {msg['content']['explanation']}")
            if msg["content"].get("result") is not None:
                st.markdown("**📊 Result:**")
                st.dataframe(msg["content"]["result"])
        else:
            st.markdown(f"**Assistant:** {msg['content']}")
