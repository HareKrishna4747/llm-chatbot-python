import streamlit as st
import os
from dotenv import load_dotenv


from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json

embeddings = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key="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"
)

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key="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"
)
