import streamlit as st
import yaml

# Safety check
if "current_dis" not in st.session_state:
    st.switch_page("main.py")

st.title(f"{st.session_state.current_dis}")



# Back button
if st.button("<- Change Disorder"):
    st.switch_page("main.py")