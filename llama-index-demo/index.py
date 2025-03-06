from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

load_dotenv()

Settings.llm = OpenAI(model="gpt-4o")

# 从指定目录读取文档数据
documents = SimpleDirectoryReader("llama-index-demo/data", recursive=True).load_data()

# 使用读取到的文档数据创建向量存储索引
index = VectorStoreIndex.from_documents(documents)

# 将索引转换为查询引擎Agent
agent = index.as_query_engine()

response = agent.query("svelte的runes的使用场景是什么?给一个demo说明")

print("response", response)

# 将索引的存储上下文持久化
index.storage_context.persist()

