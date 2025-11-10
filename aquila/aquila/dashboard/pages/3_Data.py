import streamlit as st
import pandas as pd
from aquila.tools.database import get_connection

st.set_page_config(page_title="Food Receipt Database", 
                   page_icon="📊", 
                   layout="wide")
st.title("📊 Food Receipt Database")

def load_table(name: str):
    conn = get_connection()
    df = pd.read_sql_query(f"SELECT * FROM {name}", conn)
    conn.close()
    return df

tab_orders, tab_items = st.tabs(["🧾 Orders", "🍽️ Order Items"])

with tab_orders:
    st.subheader("Orders")
    try:
        st.dataframe(load_table("orders"), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading orders: {e}")

with tab_items:
    st.subheader("Order Items")
    try:
        st.dataframe(load_table("order_items"), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading order_items: {e}")