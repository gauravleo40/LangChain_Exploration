import streamlit as st
from chain import chain


# domain = "Vegetables"



# ===================================================
#              Streamlit App FrontEnd
# ===================================================

st.title("Start-up Name and Tagline Generator")
st.divider()
domain = st.text_input("Enter the domain of your start-up", placeholder="E.g. Restaurant, Fitness, etc.")
name_provided = st.button("Generate names")
st.header(f"Domain Provided : {domain}")
st.divider()
response = chain.invoke({'domain':domain})

if name_provided:
    markdown_text = ""
    for b in response.allinfo:
        markdown_text += f"""
                            ### {b.business_name}

                            > {b.tagline}

                            ---
                        """
        
    st.markdown(markdown_text)


# st.markdown('\n'.join([f"- {i.business_name}" for i in response.allinfo]))
