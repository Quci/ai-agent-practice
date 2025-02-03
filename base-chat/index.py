from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model='gpt-4o-mini-2024-07-18',
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "您是一个帮助用户俩节鲜花信息的智能助手，并能够输出JSON格式的内容"
        },
        {
            "role": "user",
            "content": "生日送什么花最好"
        },
        {
            "role": "assistant",
            "content": "玫瑰花是生日礼物的热门选择"
        },
        {
            "role": "user",
            "content": "送货需要多长时间"
        }
    ]
)

print(response)