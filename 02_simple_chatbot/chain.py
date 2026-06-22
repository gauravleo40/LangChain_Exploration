import os
from dotenv import load_dotenv
load_dotenv()


from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# from typing import Dict, List
# from pydantic import BaseModel


# class Fields(BaseModel):
#     business_name : str
#     tagline : str

# class FieldsList(BaseModel):
#     allinfo : List[Fields]


sys_pro = """ You are an elite Cardiologist and a tenured Cardiac surgeon. You love to
        educate your patients about heart health and wellness and have a knack for simplifying
        complex medical concepts into easy-to-understand language, keeping your response very crisp. 
        Answer the user queries related ONLY to heart health and wellness.
        For non-heart related queries, politely inform refer them to the concerned specialist. 
        Keep your overall response, crisp and concise. Add a little sarcasm to your response, but do not be rude..
        
         """

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ("system", sys_pro),
    MessagesPlaceholder(variable_name = "chat_history"),
    ("human","{human_input}")
    ])

llm = ChatCohere(model = "command-r-plus-08-2024", temperature = 1)
# str_llm = llm.with_structured_output(FieldsList)

chain = prompt | llm


def chat(user_input : str):
    response = chain.invoke({"chat_history": chat_history, "human_input": user_input})
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