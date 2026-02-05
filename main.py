import streamlit as st
import yaml

# Load data
with open("router.yaml", "r") as f:
    data = yaml.safe_load(f)

st.set_page_config(page_title="Arwen DCA", layout="centered")

st.title("Diagnostic Criteria Aggregator")

cat = st.selectbox("Category", list(data.keys()))
dis = st.selectbox("Disorder", list(data[cat].keys()))

if st.button("Open Assessment"):
    # 1. Store the selection so the next page can see it
    st.session_state.current_cat = cat
    st.session_state.current_dis = dis
    st.session_state.current_dis_data = data[cat][dis]["data_path"]
    
    # 2. Forwarding Logic
    logic_type = data[cat][dis].get("logic", "simple")
    
    if logic_type == "complex":
        # Note: You must provide the path relative to the root
        st.switch_page("pages/adhd.py")
    else:
        st.switch_page("pages/simple.py")