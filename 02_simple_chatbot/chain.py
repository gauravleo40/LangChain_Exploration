import os
from dotenv import load_dotenv
load_dotenv()


from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

sys_pro = """You are a senior medical practitioner specializing in {med_spc}. You explain complex concepts in plain language and focus only on queries within {med_spc}.
If a question falls outside your specialty, politely refer the user to the appropriate specialist.
Keep answers concise and crisp. Use light sarcasm where appropriate, never rudeness.
"""

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ("system", sys_pro),
    MessagesPlaceholder(variable_name = "chat_history"),
    ("human","{human_input}")
    ])

llm = ChatCohere(model = "command-r-plus-08-2024", temperature = 1)

chain = prompt | llm


def chat(user_input : str, mc : str):
    response = chain.invoke({"med_spc" : mc, "chat_history": chat_history, "human_input": user_input})
    chat_history.append(HumanMessage(content = user_input))
    chat_history.append(AIMessage(content = response.content))
    return response.content


if __name__ == "__main__":
    print("======= Chatbot is ready. Type 'q' / 'exit' / 'quit' to exit the Chatbot =======\n")
    while True:
        user_input = input("Ask your query: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Exiting the Chatbot. Goodbye!")
            break
        else:
            doc_response = chat(user_input)
            print(doc_response)


"""
Next set of changes :
1) Currently two separate lists are used to store the chat messages. Reduce to just 1
2) Parameterize : 
    - medical specialization
    - chat style for patient age group ()
    - store previous chat threads and show in a sidebar
    - 
3)

"""