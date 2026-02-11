import streamlit as st
import yaml
from utils import add_clean_footer

# Load data
with open("router.yaml", "r") as f:
    data = yaml.safe_load(f)

st.set_page_config(page_title="Arwen DCA", layout="centered")

st.title("Arwen Diagnostic Criteria Aggregator 📋🧝‍♀️🩺")

st.error("This is **not** a diagnostic tool and should not be used as such. Please read the **About** section below for more information.", icon="🚨")

st.error("This tool is work-in-progress. Some pages may not be fully functional yet or may contain errors.", icon="🚧")

st.markdown("Select a category and disorder, then press the button below to get started:")

cat = st.selectbox(f"Category :blue-badge[{len(list(data.keys()))} available]", list(data.keys()))
dis = st.selectbox(f"Disorder :blue-badge[{len(list(data[cat].keys()))} available]", list(data[cat].keys()))

if st.button(":green[Open Diagnostic Criteria ->]"):
    st.session_state.current_cat = cat
    st.session_state.current_dis = dis
    st.session_state.current_dis_page = data[cat][dis]["page_path"]
    st.session_state.current_dis_data = data[cat][dis]["data_path"]
    
    logic_type = data[cat][dis].get("logic", "simple")
    
    if logic_type == "complex":
        st.switch_page(st.session_state.current_dis_page)
    else:
        st.switch_page("pages/simple.py")

st.markdown("## About")
st.markdown("**Arwen DCA** is designed to help clinicians aggregate diagnostic criteria based on the structure found in the DSM-5-TR. :red[This is **not** a diagnostic tool and should not be used as such]. Clinicians should always use their own judgement and verify that criteria and codes are correct.")
st.markdown("Clincians can select all diagnostic criteria that apply to their patient/client and the tool will output a list of criteria met formatted in a way that can be easily copied into an EHR or note (including systems which parse criteria to :sparkles: :rainbow[automagically*] :sparkles: create a note)")
st.markdown("This website does :green[**not store any data**] that is submitted and :green[**does not allow the input of any PHI**]. When a user refreshes a page or navigates away, all data is irrevocably lost.")
st.markdown("This project is open source and available on [GitHub](https://github.com/hermaplusplus/Arwen). It is provided under the [MIT License](https://github.com/hermaplusplus/Arwen/blob/main/LICENSE). Contributions, issue reports, feedback, and suggestions are welcome.")
st.markdown(":grey[Why is the tool called 'Arwen'? I watched Lord of the Rings recently. That's it.]")
st.markdown(":grey[:small[* Automagically, meaning using a Large Language Model.]]")

add_clean_footer() 