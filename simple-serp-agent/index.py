from dotenv import load_dotenv
from langchain import hub
from langchain_community.llms import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor


load_dotenv()

# 从 langchain 的 hub 拉取 ReAct 的提示模版
prompt = hub.pull("hwchase17/react")
print(prompt)

# 初始化LLM，确保verbose=True
llm = OpenAI()

# 初始化搜索工具，确保verbose=True
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

# 创建代理执行器并传入代理和工具，并输出运行日志
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 调用代理执行器，传入输入数据
response = agent_executor.invoke({"input": "新出的游戏《文明7》，怎么用领袖伊莎贝拉过神级难度？"})
print("输出结果：")
print(response["output"])



