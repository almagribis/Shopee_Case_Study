from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Food Online Order Insight Agent", page_icon="🔒", layout="wide")

header = "# Welcome to AI Food Online Order Insight Agent! 👋"
description = """
    Welcome to the AI Food Online Order Insight Agent Dashboard.  

For any questions or assistance, please contact **Al Magribi Sadli** at al_magribisadli@gmail.com.  

Thank you for visiting — we hope you find the insights helpful and inspiring!


"""
st.title("AI Food Online Order Insight Agent")
with st.container(border=True, height=600):
    st.header(header)
    st.markdown(description)