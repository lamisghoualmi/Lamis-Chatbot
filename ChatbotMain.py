# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:02:02 2023

@author: Benk
"""
import openai
import streamlit as st
from streamlit_chat import message


# to get api versions for my requirement when deploying
# pip list --format=freeze

# run the app on localhost from conda
# cd C:\Users\Benk\Desktop\Kaggle, Maven dataset\ChatBot
# streamlit run ChatBotMain.py


openai.api_key=st.secrets["pass"]



#This function utilizes the OpenAI Completion API to generate a response based on the given prompt. 
#The temperature setting of the API affects how random the response is. 
#A higher temperature will generate more unpredictable responses while a
 #lower temperature will lead to more predictable ones.
def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title('Lamis ChatBot  🤖 🤖')


st.sidebar.title('Lamis ChatBot  🤖 🤖')
st.sidebar.write("""
         ###### Try my  chatbot made with  openAI, GPT-3 and  Streamlit. I used Streamlit-Chat which  is simple component, which provides a chat-app like interface, which makes a chatbot deployed on Streamlit have a cool UI.
        ###### [My LinkedIn profile ](https://www.linkedin.com/in/lamisghoualmi/)
        ###### [My Github](https://github.com/lamisghoualmi/)
         """)


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You [enter your message here]: "," Hello Mr AI how was your day today? ", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')