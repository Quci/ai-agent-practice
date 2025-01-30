from dotenv import load_dotenv
from langchain import hub
from langchain_community.llms import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor

load_dotenv()
prompt = hub.pull("hwchase17/react")
print(prompt)

llm = OpenAI()

search = SerpAPIWrapper()
# 准备工具列表
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="当大模型没有相关知识时，用于搜索知识"
    ),
]

# 构建ReAct代理
agent = create_react_agent(llm, tools, prompt)

# 创建代理执行器并传入代理和工具
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 调用代理执行器，传入输入数据
print("第一次运行的结果：")
agent_executor.invoke({"input": "当前Agent最新研究进展是什么?"})
print("第二次运行的结果：")
agent_executor.invoke({"input": "当前Agent最新研究进展是什么?"})



