import streamlit as st
import yaml
from utils import add_clean_footer

# Load data
with open("router.yaml", "r") as f:
    data = yaml.safe_load(f)

st.set_page_config(page_title="Arwen DCA", layout="centered")

st.title("Diagnostic Criteria Aggregator")

st.error("This is **not** a diagnostic tool and should not be used as such. Please read the **About** section below for more information.", icon="🚨")

st.markdown("Select a category and disorder, then press the button below to get started:")

cat = st.selectbox("Category", list(data.keys()))
dis = st.selectbox("Disorder", list(data[cat].keys()))

if st.button(":green[Open Diagnostic Criteria ->]"):
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
st.markdown("This tool is designed to help clinicians aggregate diagnostic criteria based on the structure found in the DSM-5-TR. :red[This is **not** a diagnostic tool and should not be used as such]. Clinicians should always use their own judgement and verify that criteria and codes are correct.")
st.markdown("Clincians can select all diagnostic criteria that apply to their patient/client and the tool will output a list of criteria met formatted in a way that can be easily copied into an EHR or note (including systems which parse criteria to :sparkles: :rainbow[automagically*] :sparkles: create a note)")
st.markdown("This website does **not store any data** that is submitted and **does not allow the input of any Protected Health Information**. When a user refreshes a page or navigates away, all data is irrevocably lost.")
st.markdown("This project is open source and available on [GitHub](https://github.com/hermaplusplus/Arwen). It is provided under the [MIT License](https://github.com/hermaplusplus/Arwen/blob/main/LICENSE). Contributions, issue reports, feedback, and suggestions are welcome.")
st.markdown(":grey[:small[* Automagically, meaning using a Large Language Model.]]")

add_clean_footer() 