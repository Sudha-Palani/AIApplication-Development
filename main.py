#pip install -qU langchain langchain-openai langchain-google-genai streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate

import os

import streamlit as st

os.environ['GOOGLE_API_KEY']  = "AIzaSyB8zsoq9jA8-vJK3bQfjnIDiUNHBRewLwA"

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro-002")

# Create prompt template for generating LinkedIn Posts

Post_template = "Give me {number} posts on the topic of {topic}. Please make them relevant, engaging, and well-formatted for LinkedIn."

Post_prompt = PromptTemplate(template = Post_template, input_variables = ['number', 'topic'])


# Create LLM chain using the prompt template and model
Post_chain = Post_prompt | gemini_model

# Streamlit app interface

st.header("Linkedin Post")

st.subheader("Generate Posts Using Generative AI") 

# Input for the topic and number of posts

topic=st.text_input("Topic")

number=st.number_input("Number of Posts", min_value=1, max_value=10, value=1, step=1)

# Generate posts when the button is clicked

if st.button("Generate"):
    posts= Post_chain.invoke({"number" : number , "topic" : topic})
    st.write(posts.content)


