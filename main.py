import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI


st.set_page_config(page_title="Global Language Services", page_icon=":robot:", layout="centered")
st.header("Global Language Services")

col1, col2 = st.columns(2)

st.image(image='logo.png', width=500)

st.markdown("## Please enter you question")

# def get_api_key():
#     input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
#     return input_text

# openai_api_key = get_api_key()

col1, col2 = st.columns(2)
with col1:
    option_prompt = st.selectbox(
        'Which prompt do you wish to show?',
        (1,2,3))
    
with col2:
    option_tone = st.selectbox(
        'What tone of response would you like?',
        ('Formal', 'Informal'))
    
def get_text():
    input_text = st.text_area(label="Question", label_visibility='collapsed', placeholder="What is your question?...", key="text_input")
    return input_text

text_input = get_text()

if len(text_input.split(" ")) > 100:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

st.markdown("### Your Converted Email:")

if option_prompt == 1:
    template = """Answer the question based on the context below. If the
    question is related to translation, please provide the user with the link in the information.

    Context: Global Language Services provide services to simplify translations. To enable this we have packaged our services in the products below. 
    To access translation please use the following link: https://translatefile.ikea.net/dashboard

    Question: {query}
    Tone: {option_tone}

    Answer: """

elif option_prompt == 2:
    template = """Answer the question based on the context below. If the
    question is related to translatiing, please provide the user with the link in the information.

    Context: Global Language Services provide services to simplify translations. To enable this we have packaged our services in the products below. 
    To translate web pages, please follow the following link: https://vetlanda.ingka.com/

    Question: {query}
    Tone: {option_tone}

    Answer: """

else:
    template = """Answer the question based on the context below. If the
    question is related to translatiing, please provide the user with the link in the information, and information about the service, with the relevant tone.

    Context: Global Language Services provide services to simplify translations. To enable this we have packaged our services in the products below. 
    We can do file-based translations with requirements on translation quality, e.g. accuracy, IKEA tone of voice, involving translation agencies and/or IKEA proofreading.
    To use this service, please follow the following link: http://translatefile.ikea.net/

    Question: {query}
    Tone: {option_tone}

    Answer: """

st.write("Question:" + " " + text_input)

if text_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    prompt_template = PromptTemplate(input_variables=["query", "option_tone"], template=template)

    llm = OpenAI(model_name="text-davinci-003",
                    openai_api_key=st.secrets.OpenAI.key
                    )

    response = llm(template.format(query=text_input, option_tone=option_tone))

    st.write(response)
