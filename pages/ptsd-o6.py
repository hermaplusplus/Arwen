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

with open(st.session_state.current_dis_data, "r") as f:
    data = yaml.safe_load(f)

for key in data.keys():
    if key not in st.session_state:
        st.session_state[key] = False

a_score = sum(st.session_state.get(f"A{char}", False) for char in "1234")
b_score = sum(st.session_state.get(f"B{char}", False) for char in "12345")
c_score = sum(st.session_state.get(f"C{char}", False) for char in "12")
d_score = sum(st.session_state.get(f"D{char}", False) for char in "1234567")
e_score = sum(st.session_state.get(f"E{char}", False) for char in "123456")
s1_score = sum(st.session_state.get(f"S1{char}", False) for char in "12")
a_score_badge = f":red-badge[{a_score}/1]" if a_score < 1 else f":green-badge[{a_score}/1]"
b_score_badge = f":red-badge[{b_score}/1]" if b_score < 1 else f":green-badge[{b_score}/1]"
c_score_badge = f":red-badge[{c_score}/1]" if c_score < 1 else f":green-badge[{c_score}/1]"
d_score_badge = f":red-badge[{d_score}/2]" if d_score < 2 else f":green-badge[{d_score}/2]"
e_score_badge = f":red-badge[{e_score}/2]" if e_score < 2 else f":green-badge[{e_score}/2]"

st.session_state.A = a_score >= 1
st.session_state.B = b_score >= 1
st.session_state.C = c_score >= 1
st.session_state.D = d_score >= 2
st.session_state.E = e_score >= 2
st.session_state.S1 = s1_score >= 1

st.markdown("## Diagnostic Criteria")
st.info("Criteria A, B, C, D, and E will check automatically based on sub-criteria.", icon="ℹ️")

A = st.checkbox(f"A. {data['A']}\n\n{a_score_badge}", key="A", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    A1 = st.checkbox(f"1\\. {data['A1']}", key="A1")
    A2 = st.checkbox(f"2\\. {data['A2']}", key="A2")
    A3 = st.checkbox(f"3\\. {data['A3']}", key="A3")
    A4 = st.checkbox(f"4\\. {data['A4']}\n\n:orange[{data['A4note']}]", key="A4")
B = st.checkbox(f"B. {data['B']}\n\n{b_score_badge}", key="B", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    B1 = st.checkbox(f"1\\. {data['B1']}\n\n:orange[{data['B1note']}]", key="B1")
    B2 = st.checkbox(f"2\\. {data['B2']}\n\n:orange[{data['B2note']}]", key="B2")
    B3 = st.checkbox(f"3\\. {data['B3']}\n\n:orange[{data['B3note']}]", key="B3")
    B4 = st.checkbox(f"4\\. {data['B4']}", key="B4")
    B5 = st.checkbox(f"5\\. {data['B5']}", key="B5")
C = st.checkbox(f"C. {data['C']}\n\n{c_score_badge}", key="C", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    C1 = st.checkbox(f"1\\. {data['C1']}", key="C1")
    C2 = st.checkbox(f"2\\. {data['C2']}", key="C2")
D = st.checkbox(f"D. {data['D']}\n\n{d_score_badge}", key="D", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    D1 = st.checkbox(f"1\\. {data['D1']}", key="D1")
    D2 = st.checkbox(f"2\\. {data['D2']}", key="D2")
    D3 = st.checkbox(f"3\\. {data['D3']}", key="D3")
    D4 = st.checkbox(f"4\\. {data['D4']}", key="D4")
    D5 = st.checkbox(f"5\\. {data['D5']}", key="D5")
    D6 = st.checkbox(f"6\\. {data['D6']}", key="D6")
    D7 = st.checkbox(f"7\\. {data['D7']}", key="D7")
E = st.checkbox(f"E. {data['E']}\n\n{e_score_badge}", key="E", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    E1 = st.checkbox(f"1\\. {data['E1']}", key="E1")
    E2 = st.checkbox(f"2\\. {data['E2']}", key="E2")
    E3 = st.checkbox(f"3\\. {data['E3']}", key="E3")
    E4 = st.checkbox(f"4\\. {data['E4']}", key="E4")
    E5 = st.checkbox(f"5\\. {data['E5']}", key="E5")
    E6 = st.checkbox(f"6\\. {data['E6']}", key="E6")
F = st.checkbox(f"F. {data['F']}", key="F")
G = st.checkbox(f"G. {data['G']}", key="G")
H = st.checkbox(f"H. {data['H']}", key="H")

st.markdown("## Specifiers")

S1text = data["S1"].replace("With dissociative symptoms:", "**With dissociative symptoms:**")
S11text = data["S11"].replace("Depersonalization:", "**Depersonalization:**")
S12text = data["S12"].replace("Derealization:", "**Derealization:**")

st.markdown(":small[Specify whether:]")
S1 = st.checkbox(f"{S1text}", key="S1", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    S11 = st.checkbox(f"{S11text}", key="S11")
    S12 = st.checkbox(f"{S12text}", key="S12")
    st.markdown(f":orange[{data['S1note']}]")
st.markdown(":small[Specify if:]")
S2 = st.checkbox(f"{data['S2']}", key="S2")

st.markdown("## Output")

omitFGH = st.toggle("Ignore criteria F, G, and H", key="omitFGH", value=True)
omitS1 = st.toggle("Ignore dissociative symptoms specifier", key="omitS1", value=False)
omitS2 = st.toggle("Ignore delayed expression specifier", key="omitS2", value=False)

if omitFGH and not any([omitS1, omitS2]):
    st.info("Output will not include criteria F, G, and H.", icon="ℹ️")
elif omitFGH and all([omitS1, omitS2]):
    st.info("Output will not include criteria F, G, and H, nor dissociative symptoms and delayed expression specifiers.", icon="ℹ️")
elif omitFGH and any([omitS1, omitS2]):
    omitted = [o for o in [omitS1, omitS2] if o]
    omittext = ["dissociative symptoms", "delayed expression"]
    if len(omitted) == 1:
        st.info(f"Output will not include criteria F, G, and H, nor {omittext[[omitS1, omitS2].index(True)]} specifier.", icon="ℹ️")
    else:
        st.info(f"Output will not include criteria F, G, and H, nor {omittext[[omitS1, omitS2].index(True)]} and {omittext[[omitS1, omitS2].index(True, [omitS1, omitS2].index(True)+1)]} specifiers.", icon="ℹ️")
elif all([omitS1, omitS2]):
    st.info("Output will not include dissociative symptoms and delayed expression specifiers.", icon="ℹ️")
elif any([omitS1, omitS2]):
    omitted = [o for o in [omitS1, omitS2] if o]
    omittext = ["dissociative symptoms", "delayed expression"]
    if len(omitted) == 1:
        st.info(f"Output will not include {omittext[[omitS1, omitS2].index(True)]} specifier.", icon="ℹ️")
    else:
        st.info(f"Output will not include {omittext[[omitS1, omitS2].index(True)]} and {omittext[[omitS1, omitS2].index(True, [omitS1, omitS2].index(True)+1)]} specifiers.", icon="ℹ️")

if not omitFGH:
    criteria_met = all([st.session_state.get(key, False) for key in ["A", "B", "C", "D", "E", "F", "G", "H"]])
    if not criteria_met:
        unmet = [key for key in ["A", "B", "C", "D", "E", "F", "G", "H"] if not st.session_state.get(key, False)]
        st.error(f"Criteria not met: **{'**, **'.join(unmet)}**\n\n{st.session_state.current_dis} cannot be diagnosed unless all criteria A-H are met.\n\nConsider diagnosing :blue[F43.8] Other Specified Trauma- and Stressor-Related Disorder or :blue[F43.9] Unspecified Trauma- and Stressor-Related Disorder", icon="🚨")
else:
    criteria_met = all([st.session_state.get(key, False) for key in ["A", "B", "C", "D", "E"]])
    if not criteria_met:
        unmet = [key for key in ["A", "B", "C", "D", "E"] if not st.session_state.get(key, False)]
        st.error(f"Criteria not met: **{'**, **'.join(unmet)}**\n\n{st.session_state.current_dis} cannot be diagnosed unless criteria A-E are met.\n\nConsider diagnosing :blue[F43.8] Other Specified Trauma- and Stressor-Related Disorder or :blue[F43.9] Unspecified Trauma- and Stressor-Related Disorder", icon="🚨")

st.markdown(":blue-badge[Triple click anywhere in the text below to select all of it at once!]")
with st.container(border=True):
    data_out = data.copy()
    output = []
    pop = ["A", "A4note", "B", "B1note", "B2note", "B3note", "C", "D", "E", "S1", "S11", "S12", "S1note", "S2"]
    if omitFGH:
        pop.extend(["F", "G", "H"])
    for p in pop:
        data_out.pop(p, None)
    for key in data_out.keys():
        if st.session_state.get(key, False):
            output.append(data_out[key])
    if st.session_state.get("S11", False) and not omitS1:
        output.append(data["S11"].replace("Depersonalization: ", ""))
    if st.session_state.get("S12", False) and not omitS1:
        output.append(data["S12"].replace("Derealization: ", ""))
    if st.session_state.get("S2", False) and not omitS2:
        output.append(data["S2"].split(": ")[0])
    for i in range(len(output)):
        output[i] = output[i][0].lower() + output[i][1:].rstrip(".")
    st.markdown(", ".join(output))

# Back button
if st.button("<- Return to Homepage", key="backbottom"):
    st.switch_page("main.py")

add_clean_footer() 