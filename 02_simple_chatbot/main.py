import streamlit as st
# from chain import chain, chat
from chain import chat



# ===================================================
#              Streamlit App FrontEnd
# ===================================================

st.title("Hospital Chatbot : Consult your doctor")
st.divider()
# domain = st.text_input("Enter the domain of your start-up", placeholder="E.g. Restaurant, Fitness, etc.")
# begin_chat = st.button("begin_chat")
# st.header(f"Domain Provided : {domain}")
# st.divider()

# response = chain.invoke({'domain':domain})

st.header("Chatbot is ready. Type 'q' / 'exit' / 'quit' to exit the Chatbot\n")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask your query:")

if user_input:

    if user_input.lower() in ["exit", "quit", "q"]:
        st.write("==== Exiting the Chatbot. Goodbye! ====")

    else:
        st.session_state.messages.append({'role':'user','content':user_input})
        doc_response = chat(user_input)
        st.session_state.messages.append({'role':'assistant','content':doc_response})
        st.write(doc_response)

for i in st.session_state.messages :
    if i['role'] == 'user':
        st.chat_message('user').write(i['content'])
    else:
        st.chat_message('assistant').write(i['content'])

# while True:
#     user_input = st.text_input("Ask your query: ")
#     if user_input.lower() in ["exit", "quit", "q"]:
#         st.write(" ==== Exiting the Chatbot. Goodbye! ==== ")
#         break
#     else:
#         doc_response = chat(user_input)
#         st.write(doc_response)



# st.markdown('\n'.join([f"- {i.business_name}" for i in response.allinfo]))
