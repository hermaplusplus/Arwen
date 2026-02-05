import streamlit as st
import yaml
from utils import add_clean_footer

# Load data
with open("router.yaml", "r") as f:
    data = yaml.safe_load(f)

st.set_page_config(page_title="Arwen DCA", layout="centered")

st.title("Diagnostic Criteria Aggregator")

cat = st.selectbox("Category", list(data.keys()))
dis = st.selectbox("Disorder", list(data[cat].keys()))

if st.button("Open Diagnostic Criteria"):
    # 1. Store the selection so the next page can see it
    st.session_state.current_cat = cat
    st.session_state.current_dis = dis
    st.session_state.current_dis_page = data[cat][dis]["page_path"]
    st.session_state.current_dis_data = data[cat][dis]["data_path"]
    
    # 2. Forwarding Logic
    logic_type = data[cat][dis].get("logic", "simple")
    
    if logic_type == "complex":
        # Note: You must provide the path relative to the root
        st.switch_page(st.session_state.current_dis_page)
    else:
        st.switch_page("pages/simple.py")

st.markdown("## About")
st.markdown("This tool is designed to help clinicians aggregate diagnostic criteria based on the structure found in teh DSM-5-TR. :red[This is **not** a diagnostic tool and should not be used as such]. Clinicians should always sue their judgement and veri")

add_clean_footer() 