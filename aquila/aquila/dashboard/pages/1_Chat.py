import streamlit as st
from aquila.agent.agent import AgentFoodReceipt

st.set_page_config(
    page_title="Chat",
    page_icon="💬",
    layout="wide",
)

st.markdown(f"# 💬 AI Food Online Order Insight Agent")

@st.cache_resource
def initialize_agent():
    return AgentFoodReceipt()

agent_executor = initialize_agent()
content = """Welcome to AI Food Online Order Insight Agent. What can i do for you?"""
st.chat_message("assistant").write(content)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        response = agent_executor.main(query=prompt)
        if isinstance(response, str):
            st.write(response)
        else:
            st.write(response[0]["text"])