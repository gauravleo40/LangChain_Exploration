import streamlit as st
# from chain import chain, chat
from chain import chat



# ===================================================
#              Streamlit App FrontEnd
# ===================================================

st.title("Hospital Chatbot : Consult your doctor")
st.divider()

st.header("Chatbot is ready. Type 'q' / 'exit' / 'quit' to exit the Chatbot\n")

specialization = st.selectbox("Select the Medical Specialty you want to consult with:",
    ("Cardiology", "Neurology", "Orthopedics", "Dermatology", "Pediatrics", "Psychiatry"),
    index=None,
    placeholder="Select Department")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask your query:")

if user_input:

    if user_input.lower() in ["exit", "quit", "q"]:
        st.write("==== Exiting the Chatbot. Goodbye! ====")

    else:
        st.session_state.messages.append({'role':'user','content':user_input})
        doc_response = chat(user_input,specialization)
        st.session_state.messages.append({'role':'assistant','content':doc_response})
        # st.write(doc_response)

for i in st.session_state.messages :
    if i['role'] == 'user':
        st.chat_message('user').write(i['content'])
    else:
        st.chat_message('assistant').write(i['content'])
