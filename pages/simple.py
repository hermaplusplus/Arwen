import streamlit as st
import yaml
from utils import add_clean_footer

# Safety check
if "current_dis" not in st.session_state:
    st.switch_page("main.py")

st.title(f"{st.session_state.current_dis}")

# Back button
if st.button("<- Return to Homepage", key="backtop"):
    st.switch_page("main.py")



# Back button
if st.button("<- Return to Homepage", key="backbottom"):
    st.switch_page("main.py")

add_clean_footer() 