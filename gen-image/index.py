from dotenv import load_dotenv
from openai import OpenAI
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

load_dotenv()

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="哪吒三太子三打白骨精",
    size="1024x1024",
    quality="standard",
    n=1
)

images_url = response.data[0].url
response = requests.get(images_url)
img = mpimg.imread(BytesIO(response.content), format='JPG')
imgplot = plt.imshow(img)
plt.show()
