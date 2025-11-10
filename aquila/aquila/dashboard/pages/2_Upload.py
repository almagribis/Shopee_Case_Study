import streamlit as st
import base64
from typing import Dict, Any, List
from aquila.config import settings
from aquila.tools.extract import ExtractReceipt
from aquila.tools.helper import extract_json
from aquila.tools.database import insert_receipt

st.set_page_config(page_title="Food Receipt Extractor", 
                   page_icon="🍱", 
                   layout="wide")
st.title("🍱 Food Receipt Online Order Extractor")

@st.cache_resource
def initialize_agent():
    return ExtractReceipt()

exctractor = initialize_agent()

uploaded_file = st.file_uploader(
    "Upload food order receipt image",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)

if uploaded_file is not None:
    left, right = st.columns(2)
    left.image(uploaded_file, caption="Preview", width=300)
    if right.button("Process & Save"):
        try:
            image_bytes = uploaded_file.read()
            image_b64 = base64.b64encode(image_bytes).decode("utf-8")

            with st.spinner("Processing receipt (extracting data)..."):
                receipt_data_str = exctractor.main(image_b64)
                receipt_data = extract_json(receipt_data_str)

            if not isinstance(receipt_data, dict):
                st.error("Processing failed: response is not a valid JSON object.")

            # with st.spinner("Saving to database..."):
            #     insert_receipt(receipt_data, db_path=settings.db_config.db_path)

            st.success("✅ Receipt has been processed and saved to the database.")

            st.subheader("Extracted Data")
            right.json(receipt_data)

        except Exception as e:
            st.error(f"❌ Error: {e}")