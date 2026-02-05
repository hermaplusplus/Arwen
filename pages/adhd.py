import streamlit as st
import yaml

# Safety check
if "current_dis" not in st.session_state:
    st.switch_page("main.py")

with open(st.session_state.current_dis_data, "r") as f:
    data = yaml.safe_load(f)

for key in data.keys():
    if key not in st.session_state:
        st.session_state[key] = False

st.title(f"{st.session_state.current_dis}")

st.markdown("## Client Metadata")

age = st.radio("Client Age", ["Under 17", "17 or older"], key="age")
threshold = 5 if age == "17 or older" else 6

a1_score = sum(st.session_state.get(f"A1{char}", False) for char in "abcdefghi")
a2_score = sum(st.session_state.get(f"A2{char}", False) for char in "abcdefghi")
a1_score_badge = f":red-badge[{a1_score}/{threshold}]" if a1_score < threshold else f":green-badge[{a1_score}/{threshold}]"
a2_score_badge = f":red-badge[{a2_score}/{threshold}]" if a2_score < threshold else f":green-badge[{a2_score}/{threshold}]"

st.session_state.A1 = a1_score >= threshold
st.session_state.A2 = a2_score >= threshold
st.session_state.A = st.session_state.A1 or st.session_state.A2

if st.session_state.A1 and st.session_state.A2:
    S1text = [f":blue[**F90.2**] Combined presentation :green-badge[RECOMMENDED]\n\n{data['S1a']}", f":blue[**F90.0**] Predominantly inattentive presentation\n\n{data['S1b']}", f":blue[**F90.1**] Predominantly hyperactive/impulsive presentation\n\n{data['S1c']}"]
    recommended = ":blue[**F90.2**] Combined presentation"
elif st.session_state.A1:
    S1text = [f":blue[**F90.2**] Combined presentation\n\n{data['S1a']}", f":blue[**F90.0**] Predominantly inattentive presentation :green-badge[RECOMMENDED]\n\n{data['S1b']}", f":blue[**F90.1**] Predominantly hyperactive/impulsive presentation\n\n{data['S1c']}"]
    recommended = ":blue[**F90.0**] Predominantly inattentive presentation"
elif st.session_state.A2:
    S1text = [f":blue[**F90.2**] Combined presentation\n\n{data['S1a']}", f":blue[**F90.0**] Predominantly inattentive presentation\n\n{data['S1b']}", f":blue[**F90.1**] Predominantly hyperactive/impulsive presentation :green-badge[RECOMMENDED]\n\n{data['S1c']}"]
    recommended = ":blue[**F90.1**] Predominantly hyperactive/impulsive presentation"
else:
    S1text = [f":blue[**F90.2**] Combined presentation\n\n{data['S1a']}", f":blue[**F90.0**] Predominantly inattentive presentation\n\n{data['S1b']}", f":blue[**F90.1**] Predominantly hyperactive/impulsive presentation\n\n{data['S1c']}"]
    recommended = None

st.markdown("## Diagnostic Criteria")
st.info("Criteria A, A1, and A2 will check automatically based on sub-criteria.", icon="ℹ️")

A = st.checkbox(f"A. {data['A']}", key="A", disabled=True)
col1, col2 = st.columns([0.05, 0.95])
with col2:
    A1 = st.checkbox(f"1\\. {data['A1'].replace('Inattention', '**Inattention**', 1)}\n\n:orange[{data['A1note']}]\n\n{a1_score_badge}", key="A1", disabled=True)
    subcol1, subcol2 = st.columns([0.05, 0.95])
    with subcol2:
        A1a = st.checkbox(f"a. {data['A1a']}", key="A1a")
        A1b = st.checkbox(f"b. {data['A1b']}", key="A1b")
        A1c = st.checkbox(f"c. {data['A1c']}", key="A1c")
        A1d = st.checkbox(f"d. {data['A1d']}", key="A1d")
        A1e = st.checkbox(f"e. {data['A1e']}", key="A1e")
        A1f = st.checkbox(f"f. {data['A1f']}", key="A1f")
        A1g = st.checkbox(f"g. {data['A1g']}", key="A1g")
        A1h = st.checkbox(f"h. {data['A1h']}", key="A1h")
        A1i = st.checkbox(f"i. {data['A1i']}", key="A1i")
    A2 = st.checkbox(f"2\\. {data['A2'].replace('Hyperactivity and Impulsivity', '**Hyperactivity and Impulsivity**', 1)}\n\n:orange[{data['A2note']}]\n\n{a2_score_badge}", key="A2", disabled=True)
    subcol3, subcol4 = st.columns([0.05, 0.95])
    with subcol4:
        A2a = st.checkbox(f"a. {data['A2a']}", key="A2a")
        A2b = st.checkbox(f"b. {data['A2b']}", key="A2b")
        A2c = st.checkbox(f"c. {data['A2c']}", key="A2c")
        A2d = st.checkbox(f"d. {data['A2d']}", key="A2d")
        A2e = st.checkbox(f"e. {data['A2e']}", key="A2e")
        A2f = st.checkbox(f"f. {data['A2f']}", key="A2f")
        A2g = st.checkbox(f"g. {data['A2g']}", key="A2g")
        A2h = st.checkbox(f"h. {data['A2h']}", key="A2h")
        A2i = st.checkbox(f"i. {data['A2i']}", key="A2i")
B = st.checkbox(f"B. {data['B']}", key="B")
C = st.checkbox(f"C. {data['C']}", key="C")
D = st.checkbox(f"D. {data['D']}", key="D")
E = st.checkbox(f"E. {data['E']}", key="E")

st.markdown("## Specifiers")
st.info("Presentation recommendation is based on criteria A1 and A2, but you can select otherwise.", icon="ℹ️")

S1 = st.radio("Specify whether:", S1text, key="S1")
st.markdown(":small[Specify if:]")
S2 = st.checkbox(f"{data['S2']}", key="S2")
S3 = st.radio("Specify current severity:", [f":green[**Mild**]\n\n{data['S3a'].replace("Mild: ", "")}", f":orange[**Moderate**]\n\n{data['S3b'].replace("Moderate: ", "")}", f":red[**Severe**]\n\n{data['S3c'].replace("Severe: ", "")}"], key="S3")

st.markdown("## Output")

omitBCDE = st.toggle("Ignore criteria B, C, D, and E", key="omitBCDE", value=True)

if omitBCDE:
    st.info("Output will not include criteria B, C, D, and E.", icon="ℹ️")

if not omitBCDE:
    criteria_met = all([st.session_state.get(key, False) for key in ["A", "B", "C", "D", "E"]])
    if not criteria_met:
        unmet = [key for key in ["A", "B", "C", "D", "E"] if not st.session_state.get(key, False)]
        st.error(f"Criteria not met: **{'**, **'.join(unmet)}**\n\n{st.session_state.current_dis} cannot be diagnosed unless all criteria A-E are met.\n\nConsider diagnosing :blue[F90.8] Other Specified AttentionDeficit/Hyperactivity Disorder or :blue[F90.9] Unspecified Attention-Deficit/Hyperactivity Disorder", icon="🚨")
else:
    criteria_met = st.session_state.A
    if not criteria_met:
        st.error(f"Criteria not met: **A**\n\n{st.session_state.current_dis} cannot be diagnosed unless all criteria A-E are met.\n\nConsider diagnosing :blue[F90.8] Other Specified AttentionDeficit/Hyperactivity Disorder or :blue[F90.9] Unspecified Attention-Deficit/Hyperactivity Disorder", icon="🚨")

if ":green-badge[RECOMMENDED]" not in S1 and st.session_state.A:
    st.warning(f"Presentation specifier does not match recommendation. **{S1.split('\n\n')[0]}** was selected instead of **{recommended}**.", icon="⚠️")

st.markdown(":blue-badge[Triple click anywhere in the text below to select all of it at once!]")
with st.container(border=True):
    data_out = data.copy()
    output = []
    pop = ["A", "A1", "A1note", "A2", "A2note", "S1a", "S1b", "S1c", "S2", "S3a", "S3b", "S3c", "S1", "S3"]
    if omitBCDE:
        pop.extend(["B", "C", "D", "E"])
    for p in pop:
        data_out.pop(p, None)
    for key in data_out.keys():
        if st.session_state.get(key, False):
            if key == "A2c":
                output.append(data_out[key].replace("(Note:", "(note:"))
            else:
                output.append(data_out[key])
    output.append([data["S1a"], data["S1b"], data["S1c"]][S1text.index(S1)].replace(" If ", " if ", 1).replace(" Criterion ", " criterion "))
    if st.session_state.S2:
        output.append(data["S2"].replace(" Full ", " full ", 1))
    output.append([data["S3a"].replace("Few", "few", 1), data["S3b"].replace("Symptoms", "symptoms", 1), data["S3c"].replace("Many", "many", 1)][[f":green[**Mild**]\n\n{data['S3a'].replace("Mild: ", "")}", f":orange[**Moderate**]\n\n{data['S3b'].replace("Moderate: ", "")}", f":red[**Severe**]\n\n{data['S3c'].replace("Severe: ", "")}"].index(S3)])
    for i in range(len(output)):
        output[i] = output[i][0].lower() + output[i][1:].rstrip(".")
    st.markdown(", ".join(output))

# Back button
if st.button("<- Change Disorder"):
    st.switch_page("main.py")