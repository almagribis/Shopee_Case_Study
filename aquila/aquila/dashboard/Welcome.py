from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Food Online Order Insight Agent", page_icon="🔒", layout="wide")

header = "# Welcome to AI Food Online Order Insight Agent! 👋"
description = """
    This dashboard is dedicated to 

    If you have any questions or need assistance, don't hesitate to contact: **Al Magribi Sadli** - al_magribisadli@gmail.com
    
    Thank you for joining the AI Food Online Order Insight Agent! We hope you have a valuable and inspirational experience here.

"""
st.title("AI Food Online Order Insight Agent")
with st.container(border=True, height=600):
    st.header(header)
    st.markdown(description)