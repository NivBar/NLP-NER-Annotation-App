import streamlit as st
import re
from structures import NERLabel, WordStructure, OutputItem
from utils import load_inputs, save_labeled_data
from PIL import Image

logo = Image.open("logo.jpg")

LABEL_COLORS = {
    "NONE": "#A0A0A0",  # Default Gray
    "COMPANY": "#E66100",  # Orange
    "COUNTRY": "#5D3A9B",  # Deep Purple
    "DEVICE": "#FEBC11",  # Golden Yellow
    "LOCATION": "#004488",  # Dark Blue
    "OTHER": "#D3D3D3",  # Light Gray (Replaces UNKNOWN)
    "PERSON": "#882255",  # Dark Red-Purple
}

inputs = load_inputs()
if "current_index" not in st.session_state:
    st.session_state["current_index"] = 0

if "streak_count" not in st.session_state:
    st.session_state["streak_count"] = 0

if "finished" not in st.session_state:
    st.session_state["finished"] = False

if st.session_state["finished"]:
    st.title("Thank You for Annotating!")
    st.write(
        "Your annotations have been successfully saved."
        "Your contributions are invaluable. Thank you for your time and effort!"
    )
    st.balloons()
    st.stop()

current_input = inputs[st.session_state["current_index"]]
raw_words = current_input.text.split()

words = [re.sub(r"[.,!?]", "", word) for word in raw_words]

st.image(logo, width=160)  # Display logo at the top

st.title("Named Entity Recognition Annotation Tool")
st.write(
    "Label a word in the sentence on the left if it represents an entity. Select 'OTHER' if the appropriate category is not listed, and leave it unchecked if the word is not an entity."
    "You may select multiple labels for a single word, but it is recommended to choose the most appropriate one."
)

with st.sidebar:
    st.markdown(
        f"""
        <div style="background-color:#008000; padding:20px; border-radius:10px;
        font-size:24px; font-weight:bold; color:white; text-align:center;">
        {current_input.text}
        </div>
        """,
        unsafe_allow_html=True
    )

st.subheader("Label Guide")
legend_cols = st.columns(len(LABEL_COLORS))

for i, label in enumerate(sorted(LABEL_COLORS.keys())):
    with legend_cols[i]:
        st.markdown(
            f'<div style="background-color:{LABEL_COLORS[label]}; padding:8px; text-align:center; border-radius:5px; '
            f'font-size:12px; font-weight:bold; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);">{label}</div>',
            unsafe_allow_html=True,
        )

st.markdown(f'<div style="text-align:left; font-size:14px; font-weight:bold; color:green;">'
            f'Streak: {st.session_state["streak_count"]}</div>',
            unsafe_allow_html=True)

st.subheader("Annotate This Sentence")

sentence_container = st.container()
labeled_words = []

grid_size = 2

with sentence_container:
    for i in range(0, len(words), grid_size):
        word_chunk = words[i:i + grid_size]
        sentence_cols = st.columns(len(word_chunk))

        for j, word in enumerate(word_chunk):
            word_index = i + j
            word_key = f"label_{word_index}"

            if word_key not in st.session_state:
                st.session_state[word_key] = []

            selected_labels = st.session_state[word_key]

            color = LABEL_COLORS[selected_labels[0]] if selected_labels else LABEL_COLORS["NONE"]

            with sentence_cols[j]:
                st.markdown(
                    f"""
                    <div id="word_{word_index}" style="background-color:{color}; padding:15px; 
                    border-radius:5px; text-align:center; font-size:22px; font-weight:bold; 
                    min-width:120px; max-width:180px; margin-bottom:15px; margin-right:10px;
                    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);">
                    {word}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                checkbox_cols = st.columns(2)
                label_options = sorted([e.name for e in NERLabel if e.name != "NONE"])

                for col_idx in range(2):
                    with checkbox_cols[col_idx]:
                        for label in label_options[col_idx::2]:
                            is_checked = label in selected_labels
                            new_checked = st.checkbox(label, is_checked, key=f"checkbox_{word_index}_{label}")

                            if new_checked and label not in selected_labels:
                                st.session_state[word_key].append(label)
                                st.rerun()
                            elif not new_checked and label in selected_labels:
                                st.session_state[word_key].remove(label)
                                st.rerun()

                final_labels = [NERLabel[label] for label in selected_labels] if selected_labels else [NERLabel.NONE]
                labeled_words.append(
                    WordStructure(word=word, label=final_labels, position=word_index, sentence_id=current_input.ID))

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Previous Sentence", disabled=st.session_state["current_index"] == 0):
        st.session_state["current_index"] -= 1
        for i in range(len(words)):
            st.session_state[f"label_{i}"] = []
        st.rerun()

with col2:
    if st.button("Submit and Next"):
        unchecked_words = [i for i in range(len(words)) if len(st.session_state[f"label_{i}"]) == 0]

        if unchecked_words:
            if st.warning(
                    "Some words have no labels. If you continue, they will be marked as 'NONE'. Do you want to proceed?"):
                for i in unchecked_words:
                    st.session_state[f"label_{i}"] = ["NONE"]

        output = OutputItem(
            ID=str(current_input.ID),
            labeled_data=labeled_words
        )

        save_labeled_data(output)

        st.session_state["streak_count"] += 1

        if st.session_state["current_index"] < len(inputs) - 1:
            st.session_state["current_index"] += 1
            for i in range(len(words)):
                st.session_state[f"label_{i}"] = []
            st.rerun()
        else:
            st.session_state["finished"] = True
            st.rerun()
