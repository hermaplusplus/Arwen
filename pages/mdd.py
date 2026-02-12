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

st.warning("This page is :rainbow[**looooooooooong**], so this is a friendly reminder that all data is irrevocably lost when you leave or refresh the page.", icon="⚠️")

with open(st.session_state.current_dis_data, "r") as f:
    data = yaml.safe_load(f)

for key in data.keys():
    if key not in st.session_state:
        st.session_state[key] = False

a_score = sum(st.session_state.get(f"A{char}", False) for char in "123456789")
s1_score = sum(st.session_state.get(f"S1{char}", False) for char in "12345")
s2a_score = sum(st.session_state.get(f"S2A{char}", False) for char in "1234567")
s3a_score = sum(st.session_state.get(f"S3A{char}", False) for char in "12")
s3b_score = sum(st.session_state.get(f"S3B{char}", False) for char in "123456")
s4b_score = sum(st.session_state.get(f"S4B{char}", False) for char in "1234")
a_score_badge = f":red-badge[{a_score}/5]" if a_score < 5 else f":green-badge[{a_score}/5]"
s1_score_badge = f":red-badge[{s1_score}/2]" if s1_score < 2 else f":green-badge[{s1_score}/2]"
s2a_score_badge = f":red-badge[{s2a_score}/3]" if s2a_score < 3 else f":green-badge[{s2a_score}/3]"
s3a_score_badge = f":red-badge[{s3a_score}/1]" if s3a_score < 1 else f":green-badge[{s3a_score}/1]"
s3b_score_badge = f":red-badge[{s3b_score}/3]" if s3b_score < 3 else f":green-badge[{s3b_score}/3]"
s4b_score_badge = f":red-badge[{s4b_score}/1]" if s4b_score < 1 else f":green-badge[{s4b_score}/1]"

match (st.session_state.get("A1", False), st.session_state.get("A2", False)):
    case (False, False):
        a1_status_badge = ":red-badge[A1]"
        a2_status_badge = ":red-badge[A2]"
    case (True, False):
        a1_status_badge = ":green-badge[A1]"
        a2_status_badge = ":grey-badge[A2]"
    case (False, True):
        a1_status_badge = ":grey-badge[A1]"
        a2_status_badge = ":green-badge[A2]"
    case (True, True):
        a1_status_badge = ":green-badge[A1]"
        a2_status_badge = ":green-badge[A2]"

st.session_state.A = a_score >= 5 and any([st.session_state.get("A1", False), st.session_state.get("A2", False)])
st.session_state.S1 = s1_score >= 2
st.session_state.S2A = s2a_score >= 3
st.session_state.S2 = all(st.session_state.get(f"S2{char}", False) for char in "ABCD")
st.session_state.S3A = s3a_score >= 1
st.session_state.S3B = s3b_score >= 3
st.session_state.S3 = st.session_state.S3A and st.session_state.S3B
st.session_state.S4B = s4b_score >= 1

if s1_score == 2:
    s1text = [f"{data['S1A'].replace('Mild: ', ':green[**Mild**]: ')} :green-badge[RECOMMENDED]", f"{data['S1B'].replace('Moderate: ', ':orange[**Moderate**]: ')}", f"{data['S1C'].replace('Moderate-severe: ', ':red[**Moderate-severe**]: ')}", f"{data['S1D'].replace('Severe: ', ':red[**Severe**]: ')}"]
elif s1_score == 3:
    s1text = [f"{data['S1A'].replace('Mild: ', ':green[**Mild**]: ')}", f"{data['S1B'].replace('Moderate: ', ':orange[**Moderate**]: ')} :green-badge[RECOMMENDED]", f"{data['S1C'].replace('Moderate-severe: ', ':red[**Moderate-severe**]: ')}", f"{data['S1D'].replace('Severe: ', ':red[**Severe**]: ')}"]
elif s1_score >= 4:
    s1text = [f"{data['S1A'].replace('Mild: ', ':green[**Mild**]: ')}", f"{data['S1B'].replace('Moderate: ', ':orange[**Moderate**]: ')}", f"{data['S1C'].replace('Moderate-severe: ', ':red[**Moderate-severe**]: ')} :green-badge[RECOMMENDED]", f"{data['S1D'].replace('Severe: ', ':red[**Severe**]: ')} :green-badge[RECOMMENDED]"]
else:
    s1text = [f"{data['S1A'].replace('Mild: ', ':green[**Mild**]: ')}", f"{data['S1B'].replace('Moderate: ', ':orange[**Moderate**]: ')}", f"{data['S1C'].replace('Moderate-severe: ', ':red[**Moderate-severe**]: ')}", f"{data['S1D'].replace('Severe: ', ':red[**Severe**]: ')}"]

st.markdown("## Diagnostic Criteria")
st.info("Criterion A will check automatically based on sub-criteria.", icon="ℹ️")
A = st.checkbox(f"A. {data['A']}\n\n:orange[{data['Anote']}]\n\n{a_score_badge}, must include {a1_status_badge} or {a2_status_badge}", key="A", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    A1 = st.checkbox(f"1\\. {data['A1']}", key="A1")
    A2 = st.checkbox(f"2\\. {data['A2']}", key="A2")
    A3 = st.checkbox(f"3\\. {data['A3']}", key="A3")
    A4 = st.checkbox(f"4\\. {data['A4']}", key="A4")
    A5 = st.checkbox(f"5\\. {data['A5']}", key="A5")
    A6 = st.checkbox(f"6\\. {data['A6']}", key="A6")
    A7 = st.checkbox(f"7\\. {data['A7']}", key="A7")
    A8 = st.checkbox(f"8\\. {data['A8']}", key="A8")
    A9 = st.checkbox(f"9\\. {data['A9']}", key="A9")
B = st.checkbox(f"B. {data['B']}", key="B")
C = st.checkbox(f"C. {data['C']}\n\n:orange[{data['Cnote1']}]\n\n:orange[{data['Cnote2']}]", key="C")

with st.expander(":orange[Criterion C subnote on distinguishing grief from a major depressive episode]"):
    st.markdown(f":orange[{data['Cnote2sub']}]")

D = st.checkbox(f"D. {data['D']}", key="D")
E = st.checkbox(f"E. {data['E']}\n\n:orange[{data['Enote']}]", key="E")

st.markdown("## Specifiers")

S0 = st.radio("Specify whether:", options=[data['S0a'], data['S0b']], key="S0")
st.markdown(f":orange[Note: {data['CRPnote1']}]")

st.markdown(":small[Specify if:]")
S1 = st.checkbox(f"{data['S1'].replace("With anxious distress:", "**With anxious distress:**")}\n\n{s1_score_badge}", key="S1", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    S11 = st.checkbox(f"1\\. {data['S11']}", key="S11")
    S12 = st.checkbox(f"2\\. {data['S12']}", key="S12")
    S13 = st.checkbox(f"3\\. {data['S13']}", key="S13")
    S14 = st.checkbox(f"4\\. {data['S14']}", key="S14")
    S15 = st.checkbox(f"5\\. {data['S15']}", key="S15")
    col3, col4 = st.columns([0.05, 0.95])
    with col4:
        st.info("Current severity recommendation is based on criteria 1-5 above, but you can select otherwise. :red[Warning: this selection may default back to the first option if you alter criteria 1-5 above after changing it.]", icon="ℹ️")
        S1S = st.radio("Specify current severity:", options=s1text, key="S1S")
        st.markdown(f":orange[{data['S1note']}]")

st.markdown(":small[Specify if:]")
S2 = st.checkbox(f"**{data['S2']}**", key="S2", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    S2A = st.checkbox(f"A. {data['S2A']}\n\n{s2a_score_badge}", key="S2A", disabled=True)
    col3, col4 = st.columns([0.05, 0.95])
    with col4:
        S2A1 = st.checkbox(f"1\\. {data['S2A1']}", key="S2A1")
        S2A2 = st.checkbox(f"2\\. {data['S2A2']}", key="S2A2")
        S2A3 = st.checkbox(f"3\\. {data['S2A3']}", key="S2A3")
        S2A4 = st.checkbox(f"4\\. {data['S2A4']}", key="S2A4")
        S2A5 = st.checkbox(f"5\\. {data['S2A5']}", key="S2A5")
        S2A6 = st.checkbox(f"6\\. {data['S2A6']}", key="S2A6")
        S2A7 = st.checkbox(f"7\\. {data['S2A7']}", key="S2A7")
    S2B = st.checkbox(f"B. {data['S2B']}", key="S2B")
    S2C = st.checkbox(f"C. {data['S2C']}", key="S2C")
    S2D = st.checkbox(f"D. {data['S2D']}\n\n:orange[{data['S2Dnote']}]", key="S2D")

st.markdown(":small[Specify if:]")
S3 = st.checkbox(f"**{data['S3']}**", key="S3", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    S3A = st.checkbox(f"A. {data['S3A']}\n\n{s3a_score_badge}", key="S3A", disabled=True)
    col3, col4 = st.columns([0.05, 0.95])
    with col4:
        S3A1 = st.checkbox(f"1\\. {data['S3A1']}", key="S3A1")
        S3A2 = st.checkbox(f"2\\. {data['S3A2']}", key="S3A2")
    S3B = st.checkbox(f"B. {data['S3B']}\n\n{s3b_score_badge}", key="S3B", disabled=True)
    col5, col6 = st.columns([0.05, 0.95])
    with col6:
        S3B1 = st.checkbox(f"1\\. {data['S3B1']}", key="S3B1")
        S3B2 = st.checkbox(f"2\\. {data['S3B2']}", key="S3B2")
        S3B3 = st.checkbox(f"3\\. {data['S3B3']}", key="S3B3")
        S3B4 = st.checkbox(f"4\\. {data['S3B4']}", key="S3B4")
        S3B5 = st.checkbox(f"5\\. {data['S3B5']}", key="S3B5")
        S3B6 = st.checkbox(f"6\\. {data['S3B6']}", key="S3B6")
    st.markdown("\n\n".join(f":orange[{n}]" for n in data["S3Bnote"].split("\n\n")))

st.markdown(":small[Specify if:]")
S4 = st.checkbox(f"{data['S4'].replace('With melancholic features:', '**With melancholic features:**')}", key="S4", disabled=True)