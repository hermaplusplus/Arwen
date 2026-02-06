import streamlit as st
import subprocess
import platform
import os

def add_clean_footer():

    branch = os.environ.get("GIT_BRANCH", "UNKNOWN")
    branch_url = f"https://github.com/hermaplusplus/Arwen/tree/{branch}"
    commit = os.environ.get("GIT_COMMIT", "UNKNOWN")
    commit_url = f"https://github.com/hermaplusplus/Arwen/commit/{commit}"

    if branch != "UNKNOWN":
        branch = f":green-badge[**[{branch}]({branch_url})**]" if branch == "main" else f":orange-badge[**[{branch}]({branch_url})**]"
    else:
        try:
            branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
            branch = f":green-badge[**[{branch}]({branch_url})**]" if branch == "main" else f":orange-badge[**[{branch}]({branch_url})**]"
        except:
            branch = ":red-badge[UNKNOWN]"
    
    if commit != "UNKNOWN":
        commit = f":blue-badge[**[{commit}]({commit_url})**]"
    else:
        try:
            commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
            commit = f":blue-badge[**[{commit}]({commit_url})**]"
        except:
            commit = ":red-badge[UNKNOWN]"
    
    is_docker = ":green-badge[ACTIVE]" if os.path.exists('/.dockerenv') else ":red-badge[INACTIVE]"
    
    st.markdown("---")
    st.markdown(f"Made with ❤️ by [Herma](https://github.com/hermaplusplus/Arwen) | Provided under the [MIT License](https://github.com/hermaplusplus/Arwen/blob/main/LICENSE)", text_alignment="center")
    st.markdown(f"Branch: {branch}@{commit} | Docker: {is_docker} | Python: :blue-badge[{platform.python_version()}]", text_alignment="center")