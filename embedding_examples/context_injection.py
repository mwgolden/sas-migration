from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage
import json

#load api key
load_dotenv()

directory = Path("/home/matthew/Documents/my-notes/recipes")

documents = []

for file_path in directory.rglob("*"):
    if file_path.suffix in { '.md'}:
        content = file_path.read_text()
        documents.append({
            "path": str(file_path),
            "content": content
        })

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash')



system_prompt = f"""
You are a helpful assistant that answers questions about these documents: {json.dumps(documents)}
"""
# set up message for llm
messages = [
    SystemMessage(content=system_prompt)
]

while True:

    # get user query
    user_query = input("Enter your query: ")

    messages.append(HumanMessage(content=user_query))

    # invoke llm and display llm response
    response = llm.invoke(messages)

    print(response.content)

    messages.append(response)