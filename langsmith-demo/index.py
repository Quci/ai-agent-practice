from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt = ChatPromptTemplate.from_template("{location}的气候类型是？")
model= ChatOpenAI(model="gpt-4o-mini-2024-07-18")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({"location": "赞比亚"})

print(result)

