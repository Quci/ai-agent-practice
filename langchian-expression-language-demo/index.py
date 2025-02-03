from dotenv import load_dotenv
# 用于将输出结果解析为字符串
from langchain_core.output_parsers import StrOutputParser
# 用于创建聊天提示板
from langchain_core.prompts import ChatPromptTemplate
# 用于调用OpenAI公司的GPT模型
from langchain_openai import ChatOpenAI


load_dotenv()


prompt = ChatPromptTemplate.from_template("介绍{topic}的历史")

model= ChatOpenAI(model="gpt-4o-mini-2024-07-18")

output_parser = StrOutputParser()

# 使用管道操作符 (|) 连接各处理步骤
chain = prompt | model | output_parser

message = chain.invoke({"topic": "数学"})

print(message)