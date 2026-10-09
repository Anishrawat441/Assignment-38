
## Task 4: Build Streamlit code Assistant App
## Create a streamlit app with:
## 1. text area for code or prompt
## 2. Dropdown for task type:
## . Generate Code
## . Explain code
## . Debug code
## . Optimize code
## 3. Display codellama output clearly

import streamlit as st
from langchain_ollama import OllamaLLM
llm = OllamaLLM(
    model="codellama",
    temperature=0.2,
    num_predict=512,
    repeat_penalty=1.1
)

st.title("Streamlit Code Assistant App")


# Dropdown for task selection
task = st.selectbox(
    "Select Task",
    [
        "Generate Code",
        "Explain Code",
        "Debug Code",
        "Optimize Code"
    ])


# Text area for entering code or prompt
user_input = st.text_area(
    "Enter your code or prompt",
    placeholder="Paste your Python code here...",
    height=300
)

if st.button("Submit"):
    if user_input.strip():

        prompt = f"""
        Task: {task}

        Follow the selected task carefully.

        Code or Prompt:
        {user_input}
        """

        with st.spinner("CodeLlama is processing..."):
            response = llm.invoke(prompt)

        st.subheader("CodeLlama Response")
        st.markdown(response)

    else:
        st.warning("Please enter code or a prompt first.")