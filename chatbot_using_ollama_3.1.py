from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
def question_answering(input):
    template="""
    question:{question}
    Answer: let's think step by step then answer
    """
    prompt=PromptTemplate.from_template(template)
    model=OllamaLLM(model='llama3.1')
    chain=prompt | model
    ans=chain.invoke({"question":input})
    print(ans)
    return ans

st.title("chat_bot")
input=st.text_area("enter you query")
if st.button("submit"):
    if input:
      result=question_answering(input)
      with st.expander("See details"):
        st.write("Details of your input:")
        st.write(result)
    else:
        st.write("Ask me question")
