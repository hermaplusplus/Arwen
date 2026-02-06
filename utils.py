import streamlit as st
import subprocess
import platform
import os

def add_clean_footer():
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
    except:
        branch = ":red-badge[UNKNOWN]"
    
    is_docker = "Active" if os.path.exists('/.dockerenv') else "Inactive"
    
    st.markdown("---")
    st.markdown(f"Made with ❤️ by [Herma](https://github.com/hermaplusplus/Arwen) | Provided under the [MIT License](https://github.com/hermaplusplus/Arwen/blob/main/LICENSE)", text_alignment="center")
    st.markdown(f"Branch: {branch} | Docker: {is_docker} | Python: {platform.python_version()}", text_alignment="center")