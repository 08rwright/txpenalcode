# Bring in deps
import os 
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')
os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('Texas Law Guide ')
prompt = st.text_input('Example: "Define Assault" ') 

# Prompt templates
title_template = PromptTemplate(
            input_variables=['topic'],
            template='Search the Texas Penal Code for the definition, elements of offense, and punishment{topic}'
        )

script_template = PromptTemplate(
            input_variables=['title'],
            template='Texas Penal Code Title {title}'
        )

llm = OpenAI(temperature=0)

title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)

response = sequential_chain({'topic': prompt})
title = response.get('title', 'No title generated')
script = response.get('script', 'No script generated')



with st.container():
    st.write(title, script)
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .styled-box {
            background-color: #f5f5f5;
            border-radius: 5px;
            padding: 10px;
        }
        .output {
            font-family: monospace;
            font-size: 14px;
            line-height: 1.5;
            white-space: pre-wrap;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown('<div class="styled-box">', unsafe_allow_html=True)
    st.markdown(f'<pre class="output">{title}\n{script}</pre>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    