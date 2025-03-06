from dotenv import load_dotenv  # 用于加载.env文件中的环境变量（如API密钥）
from langchain import hub  # LangChain的模版中心
from langchain_community.llms import OpenAI  # OpenAI语言模型接口
from langchain_community.utilities import SerpAPIWrapper  # 搜索引擎API封装
from langchain.tools import Tool  # 工具基类（用于创建AI可使用的工具）
from langchain.agents import create_react_agent  # 创建ReAct类型代理的工厂方法
from langchain.agents import AgentExecutor  # 代理执行器

# 加载.env文件中的环境变量（需要提前在项目根目录创建.env文件存放API密钥）
load_dotenv()

# 从LangChain Hub获取预定义的ReAct提示模板（用于指导AI的思考流程）
prompt = hub.pull("hwchase17/react")
print(prompt)  # 打印模板内容供学习参考

# 初始化OpenAI大语言模型实例
# temperature=0表示关闭随机性，verbose=True显示详细运行日志
llm = OpenAI()

# 初始化搜索引擎工具（需要SerpAPI的API密钥）
# SerpAPI是Google搜索的API服务，用于获取实时网络信息
search = SerpAPIWrapper()

# 创建工具列表（当前只包含搜索工具）
tools = [
    Tool(
        name="Search",  # 工具名称
        func=search.run,  # 工具调用的方法（这里直接绑定搜索引擎的run方法）
        description="当大模型没有相关知识时，用于搜索知识"  # 关键！这个描述会帮助AI判断何时使用该工具
    ),
]

# 创建ReAct代理（将大模型、工具集和提示模板组合成智能体）
# ReAct框架原理：通过Reason（思考）和Act（行动）的循环解决问题
agent = create_react_agent(llm, tools, prompt)

# 创建代理执行器（添加了自动重试等容错机制）
# verbose=True会打印完整的思考链（Chain-of-Thought）
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 执行代理程序：询问最新游戏攻略（测试实时信息获取能力）
response = agent_executor.invoke({
    "input": "新出的游戏《文明7》，怎么用领袖伊莎贝拉过神级难度？"
})

# 打印最终输出结果
print("输出结果：")
print(response["output"])