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


user_input = st.text_input("Ask your query:")

if user_input:

    if user_input.lower() in ["exit", "quit", "q"]:
        st.write("==== Exiting the Chatbot. Goodbye! ====")

    else:
        doc_response = chat(user_input)
        st.write(doc_response)


# while True:
#     user_input = st.text_input("Ask your query: ")
#     if user_input.lower() in ["exit", "quit", "q"]:
#         st.write(" ==== Exiting the Chatbot. Goodbye! ==== ")
#         break
#     else:
#         doc_response = chat(user_input)
#         st.write(doc_response)



# st.markdown('\n'.join([f"- {i.business_name}" for i in response.allinfo]))
