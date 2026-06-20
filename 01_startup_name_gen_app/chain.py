import os
from dotenv import load_dotenv
load_dotenv()


from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from typing import Dict, List
from pydantic import BaseModel


# os.environ["COHERE_API_KEY"] = COHERE_API_KEY


class Fields(BaseModel):
    business_name : str
    tagline : str

class FieldsList(BaseModel):
    allinfo : List[Fields]


prompt = ChatPromptTemplate.from_template(
    """ You are an elite Brand Psychologist and Verbal Identity Specialist.
        Generate Three innovative start-up names for a company launching in the {domain} sector. 
        Also come up with a punchy, relevant and impactful tagline of max 7 words for each of the start-up names.
    """)

llm = ChatCohere(model = "command-r-plus-08-2024", temperature = 1)
str_llm = llm.with_structured_output(FieldsList)

chain = prompt | str_llm


if __name__ == "__main__":
    domain = "baldness treatment"
    response = chain.invoke({'domain':domain})
    for i in response.allinfo :
        print(f" Business Name : {i.business_name} ---> Tagline : {i.tagline}")